def autokey_encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            key_index += 1

            shift = ord(key_char) - ord('A')
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char

    return ciphertext

def autokey_decrypt(ciphertext, key):
    decrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            key_char = key[key_index % len(key)]
            key_index += 1

            shift = ord(key_char) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

# Example usage:
plaintext = "HELLO"
key = "N"
encrypted_text = autokey_encrypt(plaintext, key)
decrypted_text = autokey_decrypt(encrypted_text, key)

print("Plaintext:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
