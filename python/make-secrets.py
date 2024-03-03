import secrets
import string

secret_len = int(input("Set Secret Length: "))


if secret_len >= 8 and secret_len < 32:
    secret_type = str.casefold(input("Use special characters (y/n)?: "))
    if secret_type == 'y':
        secret_char = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(secret_char) for i in range(secret_len))
        print(password)
    elif secret_type == 'n':
        secret_char = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(secret_char) for i in range(secret_len))
        print(password)
elif secret_len > 8:
    print("Secret Length must be more than 8 characters.")
elif secret_len < 32:
    print("Secret Length must be less than 32 characters.")
