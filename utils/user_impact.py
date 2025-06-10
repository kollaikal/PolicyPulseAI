# utils/user_impact.py

def get_user_impact(bill, role, state):
    topics = bill.get("topics", [])
    if not topics:
        return f"No specific topics detected to personalize for a {role} in {state}."
    return f"As a {role} in {state}, you might be impacted by this bill focusing on: {', '.join(topics)}."
