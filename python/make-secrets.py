import secrets
import string

secret_len = int(input("Set Secret Length: "))
secret_type = str.casefold(input("Use special characters (y/n)?: "))

if secret_type == 'y':
    secret_char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(secret_char) for i in range(secret_len))
elif secret_type == 'n':
    secret_char = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(secret_char) for i in range(secret_len))

print(password)
