# This program implements a Caesar cipher encryption and decryption algorithm.

def encrypt(text, shift):
    # This function takes a text string and a shift value as input,
    # and returns the encrypted text.

    result = ""

    for char in text:
        # For each character in the input text, we check if it is an uppercase
        # or lowercase letter. If it is, we calculate the new character by
        # shifting the ASCII value of the character by the shift value,
        # taking the modulus of 26 to ensure that the result is still a letter,
        # and adding the ASCII value of 'A' or 'a' to get the final result.
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result

def decrypt(text, shift):
    # This function takes a text string and a shift value as input,
    # and returns the decrypted text. It does this by calling the encrypt
    # function with a shift value of 26 - shift.

    return encrypt(text, 26 - shift)

# Get user input for text and shift
text = input("\nEnter the text to be encrypted: ")
shift = int(input("\nEnter the shift value: "))

print("Text: " + text)
print("Shift: " + str(shift))
print("Cipher: " + encrypt(text, shift))

cipher = encrypt(text, shift)
print("Decrypted: " + decrypt(cipher, shift))
