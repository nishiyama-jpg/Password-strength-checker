import re

def check_password_strength(password):
    
    score = 0
    feedback = []

    # length check
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters long.")
    else:
        score += 1

    # UPPERCASE LETTERS check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # lowercase letters check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # digits/numbers check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # special characters check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Overall password strength eval
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback


if __name__ == "__main__":
    while True:
        password = input("Enter a password to check (or 'q' to quit): ")
        if password.lower() == 'q':
            break

        strength, feedback = check_password_strength(password)

        print(f"\nPassword Strength: {strength}")
        if feedback:
            print("Suggestions for improvement:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        else:
            print("Excellent password!")
        print()
