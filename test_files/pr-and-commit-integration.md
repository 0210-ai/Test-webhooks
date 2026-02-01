# Testing PR & Commit Integration

This document outlines the steps to test the "PR & Commit Integration" requirement. This feature needs to be tested manually within a Git repository.

## Setup

1.  **Create a new GitHub repository.**
2.  **Initialize the repository with a simple README.md file.**
3.  **Install and configure the submission's GitHub App or Action on the repository.**
4.  **Create a new branch for testing.**

## Test Cases

### 1. Pull Request Analysis

1.  **Create a new branch.**
2.  **Add a new file with some code that violates one of the defined policies (e.g., a security vulnerability or a style issue).**
3.  **Commit the file and push the branch to the remote repository.**
4.  **Create a new Pull Request.**
5.  **Verify that the tool automatically triggers and comments on the Pull Request with the identified issues.**
6.  **Verify that the feedback is clear and actionable.**

### 2. Commit Analysis (if supported)

1.  **If the tool supports direct commit analysis, commit a file with a policy violation directly to the main branch.**
2.  **Verify that the tool detects the issue and provides feedback (e.g., via email, a dashboard, or a failed check).**

### 3. Policy-Based Enforcement Modes

1.  **Configure the tool to operate in "blocking" mode (if supported).**
2.  **Create a Pull Request with a policy violation.**
3.  **Verify that the tool blocks the Pull Request from being merged.**
4.  **Configure the tool to operate in "advisory" mode.**
5.  **Create a Pull Request with a policy violation.**
6.  **Verify that the tool comments on the Pull Request but does not block the merge.**

### 4. Dashboard & Reporting

1.  **After running a few analysis, check the tool's dashboard (if available).**
2.  **Verify that the dashboard displays the results of the scans.**
3.  **Verify that the reports are clear and provide a good overview of the project's health.**
