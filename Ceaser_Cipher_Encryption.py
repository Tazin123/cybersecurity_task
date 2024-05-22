def encrypt_caesar(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            # Shift only alphabetic characters
            shift_amount = (ord(char) - ord('A') + shift) % 26 if char.isupper() else (ord(char) - ord('a') + shift) % 26
            if char.isupper():
                ciphertext += chr(ord('A') + shift_amount)
            else:
                ciphertext += chr(ord('a') + shift_amount)
        else:
            # Keep non-alphabetic characters unchanged
            ciphertext += char
    return ciphertext

def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)

# Example usage:
plaintext = "Hello World!"
shift = 3

encrypted_text = encrypt_caesar(plaintext, shift)
decrypted_text = decrypt_caesar(encrypted_text, shift)

print("Plain Text:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
