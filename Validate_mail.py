import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
email = input("Enter your email: ")

if validate_email(email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")