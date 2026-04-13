import asyncio
import time
import httpx
import uuid
import psutil
from jose import jwt
from typing import Dict, List
from loguru import logger

# Configuration defaults
ALGORITHM = "HS256"
SYNDICATE_DEFAULT_SECRET = "8f9a2b3c4d5e6f7a8b9c0d1e2f3a4b5c"


class SyndicateClient:
    def __init__(
        self,
        api_secret: str = SYNDICATE_DEFAULT_SECRET,
        agent_id: str = None,
        base_url: str = "http://localhost:8420",
    ):
        self.api_secret = api_secret
        self.agent_id = agent_id or f"agent_{uuid.uuid4().hex[:8]}"
        self.base_url = base_url
        self.client = httpx.AsyncClient(base_url=self.base_url)
        logger.info(
            f"Syndicate SDK Initialized: {self.agent_id} (HS256 Identity Secured)"
        )

    def _generate_token(self) -> str:
        """Internal token signing with short-lived expiration (60m)."""
        payload = {
            "iss": "syndicate.swarm",
            "sub": self.agent_id,
            "iat": int(time.time()),
            "exp": int(time.time()) + 3600,  # 1 hour
            "jti": str(uuid.uuid4()),
        }
        return jwt.encode(payload, self.api_secret, algorithm=ALGORITHM)

    async def _post(self, path: str, json: Dict) -> httpx.Response:
        token = self._generate_token()
        headers = {"Authorization": f"Bearer {token}"}
        return await self.client.post(path, json=json, headers=headers)

    # --- Core Bidding logic (Doctrine Aligned) ---

    def calculate_optimal_bid(self, lead: dict) -> int:
        """Optimal Bid = (Lead Payout * Confidence Score) - (Operating Cost + Min Margin)"""
        payout = lead.get("payout_cents", 0)
        confidence = lead.get("confidence_score", 0.0)  # From Princeton 9 match
        op_cost = 50  # Pi5 amortized cost
        min_margin = 30  # Desired margin
        min_bid_floor = 50  # Minimum marketplace bid

        bid = round((payout * confidence) - (op_cost + min_margin))
        return max(bid, min_bid_floor)

    async def place_bid(
        self, auction_id: str, amount_cents: int, poi_evidence: str = None
    ) -> bool:
        payload = {
            "auction_id": auction_id,
            "amount_cents": amount_cents,
            "poi_evidence": poi_evidence,
        }
        r = await self._post("/bid", json=payload)
        if r.status_code == 403:
            logger.error("403 Forbidden: Identity compromised or secret mismatch.")
            return False
        return r.status_code == 200

    # --- Swarm Pulse (Heartbeat) ---

    async def send_heartbeat(self):
        """Collects local telemetry and reports to the pulse aggregator."""
        try:
            # Basic system telemetry (Pi5 stats)
            cpu_percent = psutil.cpu_percent()
            temp = 45.0  # Mock temperature if sensors aren't available
            if hasattr(psutil, "sensors_temperatures"):
                temps = psutil.sensors_temperatures()
                if "cpu_thermal" in temps:
                    temp = temps["cpu_thermal"][0].current

            payload = {
                "agent_id": self.agent_id,
                "cpu_percent": cpu_percent,
                "cpu_temp_c": temp,
                "uptime_seconds": int(time.time() - psutil.boot_time()),
                "active_bids": 0,  # Placeholder for state management
                "bids_placed_last_interval": 1,
                "total_bid_cents_last_interval": 120,
                "status": "healthy",
            }

            r = await self._post("/heartbeat", json=payload)
            if r.status_code == 200:
                logger.debug(f"Heartbeat pulse success for {self.agent_id}")
                return True
        except Exception as e:
            logger.warning(f"Failed to send heartbeat: {e}")
        return False

    async def get_open_leads(self) -> List[Dict]:
        """Mock discovery endpoint for simulation."""
        # For simulation, returning a static list of Princeton 9 GEO leads
        return [
            {
                "auction_id": "auc_99",
                "category": "3d_print",
                "payout_cents": 250,
                "confidence_score": 0.9,
            },
            {
                "auction_id": "auc_101",
                "category": "seo_audit",
                "payout_cents": 500,
                "confidence_score": 0.75,
            },
        ]


async def stress_test_node(agent_id_prefix: str, duration: int = 10, interval: int = 1):
    """Small simulation routine for a single node."""
    client = SyndicateClient(agent_id=f"{agent_id_prefix}_{uuid.uuid4().hex[:4]}")
    start = time.time()
    while time.time() - start < duration:
        await client.send_heartbeat()
        leads = await client.get_open_leads()
        for lead in leads:
            bid = client.calculate_optimal_bid(lead)
            await client.place_bid(lead["auction_id"], bid)
        await asyncio.sleep(interval)


if __name__ == "__main__":
    # Test script for local verification
    asyncio.run(stress_test_node("local_sniper"))
