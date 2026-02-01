/*
Test: Enterprise Coding Standards Enforcement (Java)
Contains style violations, missing Javadocs, inconsistent naming, long lines, TODOs, and high cyclomatic complexity.
*/

public class enterprise_coding_standards_enforcement {
    // Missing class Javadoc and inconsistent naming

    // Global mutable
    public static java.util.Map<String, Object> CONFIG = new java.util.HashMap<>();

    // Tabs and long line (style violations)
    public static int DoSomething(){
	// Tabs are present on purpose to trigger lint rules
	int long_variable_name_that_exceeds_recommended_length_because_we_are_testing_line_length_violations = 1; if(long_variable_name_that_exceeds_recommended_length_because_we_are_testing_line_length_violations==1) System.out.println("This is a very long line that should exceed typical 80/120 char style limits and trigger a lint rule"); return 42; }

    // Deeply nested control flow to increase complexity
    public static int complexFunc(int x){
        if (x > 0) {
            for (int i = 0; i < 10; i++) {
                if (i % 2 == 0) {
                    for (int j = 0; j < 5; j++) {
                        if (j == 3) {
                            try {
                                x += 1;
                            } catch (Exception e) {
                                x -= 1;
                            }
                        }
                    }
                }
            }
        }
        return x;
    }

    // TODO and FIXME markers
    // TODO: replace System.out.println with logger
    // FIXME: handle edge cases

    public static int publicApi(int a, int b) {
        // Missing parameter validation and Javadocs
        return a + b;
    }

    // Configuration support: YAML and JSON rule definition files and repo-level overrides
    public static final String SAMPLE_RULES_YAML = """
rules:
  max_line_length:
    severity: warning
    value: 100
  no_tabs:
    severity: error
    enabled: true
""";

    public static final String SAMPLE_RULES_JSON = """
{
  "rules": {
    "max_line_length": { "severity": "warning", "value": 100 },
    "no_tabs": { "severity": "error", "enabled": true }
  }
}
""";

    // Note: these utilities assume common libraries (SnakeYAML, Jackson) available in enterprise environments
    public static java.util.Map<String, Object> loadRulesFromYaml(String yamlStr) {
        org.yaml.snakeyaml.Yaml yaml = new org.yaml.snakeyaml.Yaml();
        return (java.util.Map<String, Object>) yaml.load(yamlStr);
    }

    public static java.util.Map<String, Object> loadRulesFromJson(String jsonStr) throws Exception {
        com.fasterxml.jackson.databind.ObjectMapper mapper = new com.fasterxml.jackson.databind.ObjectMapper();
        return mapper.readValue(jsonStr, java.util.Map.class);
    }

    public static java.util.Map<String, Object> applyRepoOverride(java.util.Map<String, Object> rules, java.util.Map<String, Object> override) {
        java.util.Map<String, Object> merged = new java.util.HashMap<>();
        if (rules != null) merged.putAll(rules);
        java.util.Map<String, Object> rulesMap = (java.util.Map<String, Object>) merged.get("rules");
        if (rulesMap == null) rulesMap = new java.util.HashMap<>();
        java.util.Map<String, Object> overrideRules = (java.util.Map<String, Object>) override.get("rules");
        if (overrideRules != null) {
            for (java.util.Map.Entry<String, Object> e : overrideRules.entrySet()) {
                if (rulesMap.containsKey(e.getKey())) {
                    java.util.Map<String, Object> base = (java.util.Map<String, Object>) rulesMap.get(e.getKey());
                    base.putAll((java.util.Map<String, Object>) e.getValue());
                    rulesMap.put(e.getKey(), base);
                } else {
                    rulesMap.put(e.getKey(), e.getValue());
                }
            }
        }
        merged.put("rules", rulesMap);
        return merged;
    }

    public static void main(String[] args) throws Exception {
        System.out.println(DoSomething());
        java.util.Map<String, Object> rulesYaml = loadRulesFromYaml(SAMPLE_RULES_YAML);
        System.out.println("Loaded YAML rules: " + rulesYaml);
        java.util.Map<String, Object> rulesJson = loadRulesFromJson(SAMPLE_RULES_JSON);
        System.out.println("Loaded JSON rules: " + rulesJson);
        java.util.Map<String, Object> repoOverride = new java.util.HashMap<>();
        java.util.Map<String, Object> overrideRules = new java.util.HashMap<>();
        java.util.Map<String, Object> maxLine = new java.util.HashMap<>(); maxLine.put("value", 120);
        overrideRules.put("max_line_length", maxLine);
        java.util.Map<String, Object> noTabs = new java.util.HashMap<>(); noTabs.put("enabled", false);
        overrideRules.put("no_tabs", noTabs);
        repoOverride.put("rules", overrideRules);
        java.util.Map<String, Object> applied = applyRepoOverride(rulesYaml, repoOverride);
        System.out.println("After repo override: " + applied);
    }
}
