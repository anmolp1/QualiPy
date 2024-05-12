import re

def validate_email(email):
    """Validate the format of an email address."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    else:
        return False

def sanitize_input(input_string):
    """Sanitize input string to prevent XSS by removing suspicious characters."""
    sanitized = re.sub(r'[^\w\s]', '', input_string)
    return sanitized

def validate_numeric(value):
    """Validate if the input is a numeric value."""
    try:
        float(value)  # Try converting to float, which covers integers and floats
        return True
    except ValueError:
        return False

# Example usage
if __name__ == "__main__":
    # Email validation
    email = "example@domain.com"
    if validate_email(email):
        print(f"'{email}' is a valid email address.")
    else:
        print(f"'{email}' is not a valid email address.")

    # Input sanitization
    unsafe_string = "Hello, <script>alert('hack');</script>"
    safe_string = sanitize_input(unsafe_string)
    print(f"Sanitized string: {safe_string}")

    # Numeric validation
    numeric_input = "1234.56"
    if validate_numeric(numeric_input):
        print(f"'{numeric_input}' is a numeric value.")
    else:
        print(f"'{numeric_input}' is not a numeric value.")
