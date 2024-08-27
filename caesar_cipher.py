def shift_character(char, shift):
    if char.islower():
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    elif char.isupper():
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
    else:
        return char

def caesar_cipher(text, shift, mode='encrypt'):
    shift = shift % 26
    if mode == 'decrypt':
        shift = -shift

    return ''.join(shift_character(char, shift) for char in text)

def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

    if choice in ['e', 'encrypt']:
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        print(f"Encrypted Message: {caesar_cipher(message, shift, 'encrypt')}")
    elif choice in ['d', 'decrypt']:
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        print(f"Decrypted Message: {caesar_cipher(message, shift, 'decrypt')}")
    else:
        print("Invalid choice. Please enter 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()
