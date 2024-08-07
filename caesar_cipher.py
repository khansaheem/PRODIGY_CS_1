def caesar_cipher(text, shift, mode):
  """Encrypts or decrypts a given text using the Caesar Cipher algorithm.

  Args:
    text: The text to be encrypted or decrypted.
    shift: The number of positions to shift the letters.
    mode: The mode of operation, either 'encrypt' or 'decrypt'.

  Returns:
    The encrypted or decrypted text.
  """

  result = ""
  # traverse text
  for char in text:
    # Encrypt this character
    if char.isupper():
      result += chr((ord(char) + shift - 65) % 26 + 65)
    elif char.islower():
      result += chr((ord(char) + shift - 97) % 26 + 97)
    else:
      result += char
  
  if mode == 'decrypt':
    shift = -shift
    result = caesar_cipher(result, shift, 'encrypt')

  return result

text = input("Enter your message: ")
shift = int(input("Enter the shift value (1-25): "))
mode = input("Enter mode (encrypt/decrypt): ")

print("The", mode, "ed text is:", caesar_cipher(text, shift, mode))
