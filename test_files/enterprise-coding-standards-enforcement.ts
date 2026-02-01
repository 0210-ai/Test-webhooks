/*
Test: Enterprise Coding Standards Enforcement (TypeScript)
Style violations: mixed tabs, long lines, missing types, console logs in library code, TODOs, and high complexity.
*/

// Missing module docstring and inconsistent naming
export function DoSomething() {
	// Tabs used here intentionally
	const long_variable_name_that_exceeds_recommended_length_because_we_are_testing_line_length_violations = 1;
	if (long_variable_name_that_exceeds_recommended_length_because_we_are_testing_line_length_violations === 1) console.log('This is a very long line that should exceed typical 80/120 char style limits and trigger a lint rule');
	return 42;
}

// Global mutable
export let CONFIG: any = {};

// Deeply nested control flow to increase cyclomatic complexity
export function complexFunc(x: number) {
  if (x > 0) {
    for (let i = 0; i < 10; i++) {
      if (i % 2 === 0) {
        for (let j = 0; j < 5; j++) {
          if (j === 3) {
            try {
              x += 1;
            } catch (e) {
              x -= 1;
            }
          }
        }
      }
    }
  }
  return x;
}

// TODO and FIXME
// TODO: replace console.log with logger
// FIXME: handle edge cases

// Missing explicit types (any usage)
export function publicApi(a: any, b: any) {
  return a + b;
}

// Configuration support for rule definition files (YAML / JSON) and repository-level overrides
import * as fs from 'fs';
import * as yaml from 'js-yaml';

export const SAMPLE_RULES_YAML = `
rules:
  max_line_length:
    severity: warning
    value: 100
  no_tabs:
    severity: error
    enabled: true
`;

export const SAMPLE_RULES_JSON = `{
  "rules": {
    "max_line_length": { "severity": "warning", "value": 100 },
    "no_tabs": { "severity": "error", "enabled": true }
  }
}`;

export function loadRulesFromYaml(yamlStr: string) {
  return yaml.load(yamlStr);
}

export function loadRulesFromJson(jsonStr: string) {
  return JSON.parse(jsonStr);
}

// Simulated repo-level override loader (e.g., .guardrails/config.yaml)
export const REPO_OVERRIDE = {
  rules: {
    max_line_length: { value: 120 },
    no_tabs: { enabled: false }
  }
};

export function applyRepoOverride(rules: any, override: any) {
  const merged = JSON.parse(JSON.stringify(rules));
  merged.rules = merged.rules || {};
  for (const [k, v] of Object.entries(override.rules || {})) {
    merged.rules[k] = { ...(merged.rules[k] || {}), ...(v as any) };
  }
  return merged;
}

// Example exported applied rules for test harness to assert
export const APPLIED_RULES = applyRepoOverride(loadRulesFromYaml(SAMPLE_RULES_YAML), REPO_OVERRIDE);
