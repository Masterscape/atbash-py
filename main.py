import os

lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}

def convert_to_atbash(msg, key):
    cipher = ''

    for char in msg:
        if char.upper() not in lookup_table:
            cipher += increment(char, key)
            continue

        cipher += increment(lookup_table[char.upper()], key)

    return cipher

def decrypt_atbash(msg, key):
    message = ''

    for char in msg:
        letter = subtract(char, key)

        if letter not in lookup_table:
            message += letter
            continue

        message += lookup_table[letter.upper()]
    return message

def increment(char, key):
    return chr( (ord(char) + key) )

def subtract(char, key):
    return chr( ord(char) - key )

def print_ascii_values(msg):
    ascii_values = []
    for char in msg:
        ascii_values.append(ord(char))
    print(*ascii_values)

def print_options():
    print("E) Encrypt a message;")
    print("D) Decrypt a message;")
    print("Q) Close;")

def encrypt():
    message = input("Enter the message that you wish to encrypt:\n")
    key = int(input("Enter the key you wish to use:\n"))
    cipher = convert_to_atbash(message, key)
    print("The encrypted message is:", cipher)

def decrypt():
    cipher = input("Enter the message that you wish to decrypt:\n")
    key = int(input("Enter the key you wish to use:\n"))
    message = decrypt_atbash(cipher, key)
    print("The decrypted message is:", message)

def main():
    while (True):
        print_options()
        user_input = input("What would you like to do?:\n").lower()

        if (user_input == "e"):
            encrypt()
        elif (user_input == "d"):
            decrypt()
        elif (user_input == "q"):
            print("Thank you for using atbash-py")
            break
        else:
            print("Invalid input. Please try again.")

if __name__ == '__main__':
    main()