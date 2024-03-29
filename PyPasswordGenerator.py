import random
import string

def generate_password(length):
    """
    Generate a random password of given length.

    Args:
    - length (int): Length of the password to be generated.

    Returns:
    - str: The generated password.
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def get_valid_input(prompt, input_type):
    """
    Prompt the user for input of specified type.

    Args:
    - prompt (str): The message to display as prompt.
    - input_type (type): The type of input expected.

    Returns:
    - input_type: The user input.
    """
    while True:
        user_input = input(prompt)
        if user_input.strip():  # Check if input is not empty after stripping whitespace
            try:
                return input_type(user_input)
            except ValueError:
                print("Invalid input. Please try again.")
        else:
            print("Input cannot be empty. Please try again.")

def main():
    """
    Main function to execute the password generator.
    """
    print("Welcome To Your Password Generator")

    number = get_valid_input("Amount of passwords to generate: ", int)
    length = get_valid_input("Input your password length: ", int)

    print("\nHere are your passwords: ")
    for _ in range(number):
        password = generate_password(length)
        print(password)

if __name__ == "__main__":
    main()
