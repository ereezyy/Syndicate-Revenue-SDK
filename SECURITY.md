# Security Policy

## Supported Versions

Only the following versions of the Syndicate Swarm (WaveForge server, AgentSDK, and related components) are currently supported with security updates:

| Version | Supported |
|------------------|--------------------|
| 1.x (main) | :white_check_mark: |
| 1.0-soul | :white_check_mark: |
| < 1.0 | :x: |

**Note**: Development and pre-1.0 experimental branches (including any Pi5 cluster prototypes) receive no security backports. Always run the latest stable release from the main branch or tagged releases.

## Reporting a Vulnerability

The Syndicate Swarm team takes security seriously — especially around identity integrity, JWT signing, heartbeat telemetry, bidding logic, and protection against rogue nodes or marketplace compromise.

If you discover a security vulnerability (e.g., issues with HS256 JWT-Lite validation, unauthorized agent provisioning, heartbeat protocol weaknesses, WebSocket exposure, or any bypass of the signed identity layer), please report it responsibly.

### How to Report
- **Preferred method**: Email **eddy@syndicate.swarm** (or Signal: eddywoods.01 for encrypted reports).
- Include the following in your report:
  - Clear description of the vulnerability
  - Steps to reproduce (including any test scripts or PoC if safe)
  - Affected component (e.g., `syndicate.py`, JWT validation, `/heartbeat` endpoint, AgentSDK client, Docker Swarm stack, etc.)
  - Potential impact (e.g., rogue node spoofing, telemetry saturation, bid manipulation)
  - Any suggested mitigation

**Do not** open a public GitHub issue or pull request discussing the vulnerability.

### What to Expect
- **Acknowledgment**: We will confirm receipt of your report within **48 hours** (usually much faster).
- **Updates**: You can expect status updates at least every **7 days** while we investigate and fix the issue.
- **Timeline**: Critical issues (e.g., identity spoofing or remote code execution) will be addressed with high priority. We aim to release a patch within **14 days** for high-severity findings.
- **Credit**: We will publicly credit responsible reporters (unless you prefer to remain anonymous) once the vulnerability is fixed and disclosed.
- **Declined reports**: If the issue is out of scope, already known, or does not meet our definition of a security vulnerability, we will explain why.

### Disclosure Policy
We practice **coordinated disclosure**. We ask that you do not publicly disclose the vulnerability until we have had reasonable time to investigate and release a fix (typically 30–90 days depending on severity). We will work with you on a mutually agreed disclosure date.

### Out of Scope
- Issues in unsupported versions (< 1.0)
- Social engineering, physical attacks, or attacks requiring physical access to Pi5 hardware
- Denial-of-service via intentional flood from outside the simulated stress-test framework
- Any "black hat" GEO tactics that violate the SOUL.md ethical guardrails

### Additional Notes
- All production nodes must use signed HS256 identities generated via `scripts/generate_agent_identity.py`.
- The swarm operates under the **SOUL.md** doctrine: identity integrity is non-negotiable, and any rogue behavior results in immediate exclusion from the settlement pool.

Thank you for helping keep the Syndicate Swarm secure and professional.

**Directive Overseer**: Dr. NigHammer
**Creator**: Eddy Woods
