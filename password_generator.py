import random
import string


def generatePassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Welcome to password generator!!")
    length = int(input("Enter the desired password length: "))

    if length < 6:
        print("Password must be of atleast 6 char")

    else:
        password = generatePassword(length)
        print(f"Your generated password: {password}")


if __name__ == "__main__":
    main()
