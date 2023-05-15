import re
def is_acceptable_password(password: str) -> bool:
    password_size = len(password)
    password_with_number = bool(re.search('r\d',password))

    if (password_size > 9) and not password.isdigit():
        return True
    elif (password_size > 6) and password_with_number and not password.isdigit():
        return True
    else:
        return False

print("Example:")
print(is_acceptable_password("short"))

# These "asserts" are used for self-checking
assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("notshort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")