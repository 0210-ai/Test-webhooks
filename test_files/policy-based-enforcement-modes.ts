/*
Test: Policy-Based Enforcement Modes (TypeScript)
Includes guardrails pragmas and annotated exemptions for testing allow/monitor/deny behavior.
*/

// guardrails: allow=hardcoded-secret reason="testing-exemption"
export const ADMIN_PASSWORD = 'hunter2';

// guardrails: mode=monitor
export function maybeInsecureAction() {
  // This action should be flagged in enforce mode but allowed in monitor mode
  return 'performed risky action';
}

// guardrails: deny=unapproved-library
import unapprovedInternalLib from 'unapproved-internal-lib'; // import to be denied in enforce mode

export function callUnapproved() {
  return unapprovedInternalLib.doThing();
}
