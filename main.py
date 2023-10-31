def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(password):
    new_password = ""
    for digit in password:
        new_digit = str(int(digit) + 3)
        new_password += new_digit
    return new_password


def main():
    choice = 0
    while choice != 3:
        menu()
        choice = int(input("\nPlease enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            encode(password)
        elif choice == 2:
            pass
        elif choice == 3:
            exit()


if __name__ == "__main__":
    main()
