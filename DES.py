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
