"""
Test: License & IP Compliance
Contains snippets copied from third-party code with conflicting/absent license headers, and embedded license text to trigger license scanners.
"""

# A copy-pasted snippet with a GPL header (simulated)
# ==================================================================
# This file includes parts of code originally under GPLv2.
# Copyright (c) 2001 SomeProject
# License: GPL-2.0-only
# ==================================================================

# Another snippet missing license header which may be proprietary
def third_party_algorithm(x):
    # This algorithm was copied from external vendor docs and lacks an SPDX header
    return x * 2  # proprietary logic

# A file with mismatched license tag
__license__ = "MIT"  # but contains GPL code above

if __name__ == '__main__':
    print('license-ip-compliance test file loaded')
