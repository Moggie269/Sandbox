"""CP1404 prac_02 - Password stars"""

def main():
    minimum_length = int(input('Enter minimum length: '))
    password = get_valid_password("Insert password: ", minimum_length)
    print("*" * len(password))


def get_valid_password(prompt, minimum_length):
    password = input(prompt)
    while len(password) < minimum_length:
        print("Invalid password")
        password = input(prompt)
    return password


main()