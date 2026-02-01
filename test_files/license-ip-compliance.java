/*
Test: License & IP Compliance (Java)
Contains mixed license headers and conflicting license metadata to trigger license scanners.
*/

// ==================================================================
// This file includes parts of code originally under GPLv2.
// Copyright (c) 2001 SomeProject
// License: GPL-2.0-only
// ==================================================================

public class license_ip_compliance {
    // Another snippet missing license header which may be proprietary
    public static int thirdPartyAlgorithm(int x) {
        // This algorithm was copied from external vendor docs and lacks an SPDX header
        return x * 2; // proprietary logic
    }

    // Mismatched license tag
    public static final String __license__ = "MIT"; // but contains GPL code above

    public static void main(String[] args) {
        System.out.println("license-ip-compliance Java test loaded");
    }
}
