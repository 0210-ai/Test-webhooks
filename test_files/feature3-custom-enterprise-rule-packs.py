"""
Test: Feature 3 - Custom Enterprise Rule Packs
Contains enterprise-only patterns (internal api names, proprietary markers) which should be recognized by custom rule packs.
"""

# Internal-only API usage (should be blocked unless allowed by policy)
from acme_proprietary import secret_connect

# Enterprise-specific resource tag
RESOURCE_TAG = "ACME-ONLY: do not export"

# Proprietary naming that custom rules might flag
acme_privilege_key = "priv-001"

def call_internal_service():
    # This should be detected by enterprise-specific rule packs
    return secret_connect(RESOURCE_TAG)

if __name__ == '__main__':
    print(call_internal_service())
