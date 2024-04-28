#This implementation follows the steps outlined:

#1. Generate DES Key: The generate_des_key function creates a DES key securely using get_random_bytes.

#2. Create a Cipher Instance: The DES.new function is used to create a DES cipher instance with the specified key and mode (ECB in this case).

#3. Convert String to Byte[] Array: The _pad_message function converts the plaintext message from string format to a byte array format and pads it to make its length a multiple of 8 bytes.

#4.  Encryption: The encrypt_message function initializes the cipher in encryption mode and encrypts the plaintext message.

#5. Decryption: The decrypt_message function initializes the cipher in decryption mode and decrypts the ciphertext back to the original plaintext.
#pip install pycryptodome


from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

def generate_des_key():
    return get_random_bytes(8)  # DES key size is 8 bytes

def encrypt_message(message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_message = _pad_message(message)
    ciphertext = cipher.encrypt(padded_message)
    return base64.b64encode(ciphertext).decode()

def decrypt_message(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = base64.b64decode(ciphertext)
    decrypted_message = cipher.decrypt(ciphertext)
    return _unpad_message(decrypted_message)

def _pad_message(message):
    padding_length = 8 - (len(message) % 8)
    padded_message = message + bytes([padding_length] * padding_length)
    return padded_message

def _unpad_message(message):
    padding_length = message[-1]
    return message[:-padding_length]

# Example usage:
if __name__ == "__main__":
    # Generate DES key
    des_key = generate_des_key()

    # User message to be encrypted
    user_message = "This is a secret message."

    # Encrypt the message
    encrypted_message = encrypt_message(user_message.encode(), des_key)
    print("Encrypted message:", encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, des_key)
    print("Decrypted message:", decrypted_message)
