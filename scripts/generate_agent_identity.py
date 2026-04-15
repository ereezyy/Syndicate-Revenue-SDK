import time
import uuid
import argparse
from jose import jwt

# from loguru import logger

# Configuration defaults - Aligned with Phase 3 Server
ALGORITHM = "HS256"
SYNDICATE_DEFAULT_SECRET = "8f9a2b3c4d5e6f7a8b9c0d1e2f3a4b5c"


def generate_signed_token(agent_id: str, secret: str = SYNDICATE_DEFAULT_SECRET) -> str:
    """Creates a production-hardened HS256 identity token for a swarm node."""
    payload = {
        "iss": "syndicate.swarm",
        "sub": agent_id,
        "iat": int(time.time()),
        "exp": int(time.time()) + 31536000,  # 1 year for node persistence
        "jti": str(uuid.uuid4()),
        "node_type": "sniper",
        "swarm_version": "1.0-soul",
    }
    return jwt.encode(payload, secret, algorithm=ALGORITHM)


def main():
    parser = argparse.ArgumentParser(
        description="s Syndicate Swarm: Agent Identity Generator (Phase 3 Hardening)"
    )
    parser.add_argument(
        "--id", help="Custom Agent ID (if blank, UUID generated)", default=None
    )
    parser.add_argument(
        "--secret",
        help="Syndicate API Secret (Internal)",
        default=SYNDICATE_DEFAULT_SECRET,
    )
    args = parser.parse_args()

    agent_id = args.id or f"agent_{uuid.uuid4().hex[:8]}"
    token = generate_signed_token(agent_id, args.secret)

    print("-" * 50)
    print("SYNDICATE AGENT IDENTITY PROVISIONED")
    print("-" * 50)
    print(f"Agent ID: {agent_id}")
    print(f"Token (JWT-Lite HS256): \n\n{token}\n")
    print("-" * 50)
    print(
        "Action: Save this token to your .env or SYNDICATE_API_KEY environment variable."
    )
    print("The Syndicate Swarm expects this token in all machine-to-machine requests.")
    print("-" * 50)


if __name__ == "__main__":
    main()
