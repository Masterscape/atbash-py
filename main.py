import os
clear_command = ('cls' if os.name == 'nt' else 'clear')

lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}

def clear():
    global clear_command
    os.system(clear_command)

def convert_to_atbash(message, key):
    ciphertext = ''

    for char in message:
        if char.upper() not in lookup_table:
            ciphertext += increment(char, key)
            continue

        ciphertext += increment(lookup_table[char.upper()], key)

    return ciphertext

def decrypt_atbash(ciphertext, key):
    message = ''

    for char in ciphertext:
        letter = decrement(char, key)

        if letter not in lookup_table:
            message += letter
            continue

        message += lookup_table[letter.upper()]
    return message

def increment(char, key):
    return chr( (ord(char) + key) )

def decrement(char, key):
    return chr( ord(char) - key )

def print_options():
    print("E) Encrypt a message;")
    print("D) Decrypt a message;")
    print("Q) Close;")

def encrypt():
    message = input("Enter the message that you wish to encrypt:\n")
    key = int(input("Enter the key you wish to use (0 means there will be no key applied):\n"))
    ciphertext = convert_to_atbash(message, key)
    clear()
    print("The encrypted message is:", ciphertext, '\n')

def decrypt():
    ciphertext = input("Enter the message that you wish to decrypt:\n")
    key = int(input("Enter the key you wish to use (0 means there will be no key applied):\n"))
    message = decrypt_atbash(ciphertext, key)
    clear()
    print("The decrypted message is:", message, '\n')

def main():
    while (True):
        print_options()
        user_input = input("What would you like to do?:\n").lower()

        clear()

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