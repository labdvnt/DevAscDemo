# myfeature.py
# This script demonstrates a simple feature implementation.

def greet_user(name):
    """
    Function to greet the user with their name.
    :param name: str - Name of the user
    :return: str - Greeting message
    """
    return f"Hello, {name}! Welcome to the feature demo."

if __name__ == "__main__":
    # Example usage
    user_name = input("Enter your name: ")
    print(greet_user(user_name))
    print("This is my feature script.")
    print("Welcome to the DevAsc feature demo!")