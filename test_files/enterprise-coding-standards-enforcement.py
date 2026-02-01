"""
Test: Enterprise Coding Standards Enforcement
Contains style violations, missing docstrings, inconsistent naming, extremely long lines, TODOs, and undesired globals / prints for library code.
"""

# Missing module docstring and inconsistent naming
def DoSomething():
	# tabs are present. Many style guides forbid tabs
	long_variable_name_that_exceeds_recommended_length_because_we_are_testing_line_length_violations = 1
	if long_variable_name_that_exceeds_recommended_length_because_we_are_testing_line_length_violations == 1: print('This is a very long line that should exceed typical 80/120 char style limits and trigger a lint rule')
	return 42

# Global mutable
CONFIG = {}

# Deeply nested function to create high cyclomatic complexity
def complex_func(x):
    if x > 0:
        for i in range(10):
            if i % 2 == 0:
                for j in range(5):
                    if j == 3:
                        try:
                            x += 1
                        except Exception:
                            x -= 1
    return x

# TODO and FIXME markers
# TODO: replace print with logger
# FIXME: handle edge cases

# Missing type hints on public API
def public_api(a, b):
    return a + b

# Configuration examples to verify rule-loading behavior
# Sample rules definition (YAML)
SAMPLE_RULES_YAML = '''
rules:
  max_line_length:
    severity: warning
    value: 100
  no_tabs:
    severity: error
    enabled: true
'''

# Sample rules definition (JSON)
SAMPLE_RULES_JSON = '''
{
  "rules": {
    "max_line_length": { "severity": "warning", "value": 100 },
    "no_tabs": { "severity": "error", "enabled": true }
  }
}
'''

def load_rules_from_yaml(yaml_str):
    import yaml
    return yaml.safe_load(yaml_str)

def load_rules_from_json(json_str):
    import json
    return json.loads(json_str)

# Simulate repository-level override (e.g., .guardrails/config.yaml in a repo)
REPO_OVERRIDE = {
    "rules": {
        "max_line_length": {"value": 120},
        "no_tabs": {"enabled": False}
    }
}

def apply_repo_override(rules, override):
    # Merge override into rules['rules'] with override precedence
    merged = {k: dict(v) for k, v in rules.items()} if isinstance(rules, dict) else dict(rules)
    for rule_name, rule_vals in override.get('rules', {}).items():
        if 'rules' not in merged:
            merged['rules'] = {}
        if rule_name in merged['rules']:
            merged['rules'][rule_name].update(rule_vals)
        else:
            merged['rules'][rule_name] = rule_vals
    return merged

if __name__ == '__main__':
    print(DoSomething())
    rules = load_rules_from_yaml(SAMPLE_RULES_YAML)
    print('Loaded YAML rules:', rules)
    rules_json = load_rules_from_json(SAMPLE_RULES_JSON)
    print('Loaded JSON rules:', rules_json)
    applied = apply_repo_override(rules, REPO_OVERRIDE)
    print('After applying repo override:', applied)
