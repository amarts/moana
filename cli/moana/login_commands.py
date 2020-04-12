

def set_args(subparser):
    login_parser = subparser.add_parser('login')
    login_parser.add_argument("username", help="Username or Email")


def main(_args):
    # TODO: Implement this Once Login API available
    print("Logged in Successfully")
