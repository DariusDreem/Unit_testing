
simple_passwords = {"password", "123456", "123456789", "qwerty", "abc123", "football", "monkey", "letmein", "111111", "1234", "Password123"}


def test_length(password, min_length, max_length=None):
    if max_length is not None:
        return min_length <= len(password) <= max_length
    return len(password) >= min_length

def test_uppercase(password):
    return any(char.isupper() for char in password) 

def test_lowercase(password):
    return any(char.islower() for char in password) 

def test_digit(password):
    return any(char.isdigit() for char in password)

def test_special_character(password):
    return any(char in "@#$%^&+=" for char in password)


def test_no_whitespace(password):
    return not any(char.isspace() for char in password)


def test_no_identical_characters(password, length=3):
    for i in range(len(password) - length + 1):
        if password[i:i+length] == password[i] * length:
            return False
    return True
    
def check_simple_password(password):
    return password in simple_passwords

def basic_test(password):
    rules = [
        test_length(password, 8),
        test_uppercase(password),
        test_lowercase(password),
        test_digit(password)
    ]
    return all(rules)

def intermediate_test(password):
    rules = [
        test_length(password, 8, 20),
        test_uppercase(password),
        test_lowercase(password),
        test_digit(password),
        test_special_character(password),
        test_no_whitespace(password),
        test_no_identical_characters(password)
    ]
    return all(rules)
    
def advanced_test(password):
    if check_simple_password(password):
        return "Too Simple"
    rules = [
        test_uppercase(password),
        test_lowercase(password),
        test_digit(password),
        test_special_character(password),
    ]
    match sum(rules)/len(rules) * 100:
        case x if x < 20:
            return "Very Weak"
        case x if x > 20 and x < 40:
            return "Weak"
        case x if x > 40 and x < 60:
            return "Medium"
        case x if x > 80 and x < 100:
            return "Strong"
        case 100:
            return "Very Strong"
            