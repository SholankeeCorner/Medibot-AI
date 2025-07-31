def get_response(user_input: str) -> str:
    if "fever" in user_input.lower():
        return "Please monitor your temperature and stay hydrated."
    return "I'm not sure. Can you tell me more about your symptoms?"