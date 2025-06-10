# utils/user_impact.py

def get_user_impact(bill, role, state):
    """
    Generate a personalized impact statement for the user based on their role and state.
    :param bill: dict with bill data, including 'topics' list.
    :param role: str, user role like 'Parent', 'Veteran', 'Student'
    :param state: str, US state abbreviation like 'CA', 'NY'
    :return: str, personalized impact summary
    """
    topics = bill.get("topics", [])
    
    if not topics:
        return f"As a {role} in {state}, there is no specific topic in this bill that directly impacts you based on current data."

    # Example placeholders for future fine-grained logic with census/demographic data
    # For now, just create user-friendly message:
    topic_list = ", ".join(topics)
    impact_message = (
        f"As a {role} living in {state}, this bill may affect you through policies related to: {topic_list}. "
        "Consider reviewing benefits, tax changes, or regulations in these areas. "
        "You can also contact your local representatives to learn more or express your views."
    )

    return impact_message
