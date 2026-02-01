/*
Test: License & IP Compliance (TypeScript)
Contains snippets with GPL header and conflicting license indication to trigger license scanners.
*/

// ==================================================================
// This file includes parts of code originally under GPLv2.
// Copyright (c) 2001 SomeProject
// License: GPL-2.0-only
// ==================================================================

export function thirdPartyAlgorithm(x: number) {
  // Copied from vendor docs, lacks SPDX header (proprietary)
  return x * 2; // proprietary logic
}

// Mismatched license tag
export const __license__ = 'MIT'; // but contains GPL code above
