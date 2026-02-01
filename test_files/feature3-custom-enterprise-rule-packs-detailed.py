# Example of a custom rule definition (for context):
#
# rules:
#   - id: max-function-arguments
#     message: "Functions should not have more than 3 arguments."
#     severity: "warning"
#     language: "python"
#     pattern: |
#       def $FNAME($ARG1, $ARG2, $ARG3, $ARG4, ...):
#         ...

# This function violates the custom rule "max-function-arguments"
def process_user_data(user_id, name, email, address, phone_number):
    """
    This function takes too many arguments and should be refactored.
    """
    print(f"Processing data for user {user_id}: {name}, {email}, {address}, {phone_number}")
    # ... business logic ...

# This function is compliant with the custom rule
def get_user_by_id(user_id):
    """
    This function is compliant with the custom rule.
    """
    print(f"Getting user with id {user_id}")
    # ... business logic ...
