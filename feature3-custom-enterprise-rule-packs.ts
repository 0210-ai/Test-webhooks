/*
Test: Feature 3 - Custom Enterprise Rule Packs (TypeScript)
Includes enterprise-only identifiers and internal module usage to be flagged by custom rule packs.
*/

import { secretConnect } from 'acme-proprietary';

export const RESOURCE_TAG = 'ACME-ONLY: do not export';
export const acmePrivilegeKey = 'priv-001';

export function callInternalService() {
  // Enterprise-specific call that should be blocked without proper allowance
  return secretConnect(RESOURCE_TAG);
}
