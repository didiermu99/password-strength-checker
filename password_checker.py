import re

def check_password_strength(password):
    """
    Checks the strength of the given password and returns feedback.
    """
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ @!#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password) is None

    # Strength calculation
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    error_count = sum(errors)

    # Print detailed feedback
    if length_error:
        print("Password should be at least 8 characters long.")
    if digit_error:
        print("Password should include at least one digit.")
    if uppercase_error:
        print("Password should include at least one uppercase letter.")
    if lowercase_error:
        print("Password should include at least one lowercase letter.")
    if symbol_error:
        print("Password should include at least one special character (e.g., @, #, $, etc.).")

    # Return strength level
    if error_count == 0:
        return "Strong"
    elif error_count <= 2:
        return "Moderate"
    else:
        return "Weak"

if __name__ == "__main__":
    # Ask user to enter a password
    password = input("Enter a password to check its strength: ")
    print("\nAnalyzing password strength...\n")
    strength = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")
