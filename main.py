# encode() by Spencer Sturman
# decode() by Collin Williams

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


def encode(password):
    new_password = ""
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        new_password += new_digit
    return new_password

def decode(password):
    decoded_password = ""
    for digit in password:
        decoded_password += str((int(digit) - 3) % 10)
    return decoded_password

def main():
    choice = 0
    stored_password = ''
    while choice != 3:
        menu()
        choice = int(input("\nPlease enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
            stored_password = encode(password)
        elif choice == 2:
            original_password = decode(stored_password)
            print(f"The encoded password is {stored_password}, and the original password is {original_password}.")
        elif choice == 3:
            exit()


if __name__ == "__main__":
    main()
