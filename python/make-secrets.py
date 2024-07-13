import secrets
import string
import argparse


def special_character_secret(secret_length=8):
    sp_secret = ''.join(secrets.choice(string.ascii_letters + string.digits +
                                       string.punctuation)
                        for i in range(secret_length))
    print(sp_secret)


def alpha_num_secret(secret_length=8):
    n_secret = ''.join(secrets.choice(string.ascii_letters + string.digits)
                       for i in range(secret_length))
    print(n_secret)


parser = argparse.ArgumentParser(description="""Generate random secrets.
                                  If no character length is provided,
                                  the default is 8 characters.""")
parser.add_argument("-s", "--special", action="store_const",
                    const=special_character_secret,
                    help="Secret with special characters.")
parser.add_argument("-n", "--normal", action="store_const",
                    const=alpha_num_secret,
                    help="Alphanumeric secret.")
parser.add_argument("-l", "--length", help="Set secret length", type=int,
                    default=8)
args = parser.parse_args()


if args.special:
    special_character_secret(args.length)
elif args.normal:
    alpha_num_secret(args.length)
