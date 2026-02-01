"""
Test: Feature 5 - Dashboard & Reporting (Optional / Bonus)
This file contains multiple small, varied issues to test aggregation and reporting across categories.
"""

# Hardcoded secret
DB_PASSWORD = "P@ssw0rd123"

# TODO markers and FIXME
# TODO: remove debug code
# FIXME: fix race condition

# Minor style issues
def fn(a,b): return a+b

# Possible leakage: prints of PII
def log_user(user):
    print(f"User login: {user['email']} password={user.get('password')}")

# Performance smell: building string ineffectively
s = ''
for i in range(1000):
    s += str(i)

if __name__ == '__main__':
    print('feature5-dashboard-reporting-optional test file loaded')
