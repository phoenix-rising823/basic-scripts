import secrets
import string


class SecreLengthError(Exception):
    "Raised when Secret Length isn't between 8 and 32 characters"
    pass


try:
    secret_len = int(input("Set Secret Length: "))
    if secret_len < 8 or secret_len > 32:
        raise SecreLengthError
except SecreLengthError:
    print("Secret Length must be between 8 and 32 characters...")
except (TypeError, ValueError):
    print("A valid value between 8 and 32 characters must be entered...")
else:
    secret_type = str.casefold(input("Use special characters (y/n)?: "))
    if secret_type == 'y':
        secret_char = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(secret_char) for i in range(secret_len))
        print(password)
    elif secret_type == 'n':
        secret_char = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(secret_char) for i in range(secret_len))
        print(password)
