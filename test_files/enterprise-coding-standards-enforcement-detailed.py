# Inconsistent Naming
def calculateTotal(price, quantity):
    TAX_RATE = 0.08
    total_price = price * quantity
    taxAmount = total_price * TAX_RATE
    return total_price + taxAmount

class user_manager:
    def __init__(self, users):
        self.all_users = users

    def FindUser(self, userId):
        for u in self.all_users:
            if u.id == userId:
                return u
        return None

# Magic Numbers
def check_status(status):
    if status == 1: # Magic number for "Active"
        return "Active"
    elif status == 2: # Magic number for "Inactive"
        return "Inactive"
    return "Unknown"

# Long Function
def process_data(data):
    # Step 1: Validate the data
    if not isinstance(data, list):
        raise ValueError("Data must be a list")
    if len(data) == 0:
        return None

    # Step 2: Filter out negative numbers
    filtered_data = [x for x in data if x >= 0]

    # Step 3: Calculate the sum
    total = sum(filtered_data)

    # Step 4: Calculate the average
    average = total / len(filtered_data)

    # Step 5: Normalize the data
    max_value = max(filtered_data)
    normalized_data = [x / max_value for x in filtered_data]

    # Step 6: Convert to a string
    result_str = ",".join(map(str, normalized_data))

    # Step 7: Log the result
    print("Processed data: " + result_str)

    # Step 8: Return a dictionary with all the results
    return {
        "filtered_data": filtered_data,
        "total": total,
        "average": average,
        "normalized_data": normalized_data,
        "result_str": result_str
    }
