dict1 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
         'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
         'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
         'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
         'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}

dict2 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
         5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J',
         10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O',
         15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T',
         20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}


def rail_fence_encrypt(text, key):

    rail = [['\n' for i in range(len(text))]
                for j in range(key)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = text[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))


def generate_auto_key(message, key):
    i = 0
    while True:
        if len(key) == len(message):
            break
        if message[i] == ' ':
            i += 1
        else:
            key += message[i]
            i += 1
    return key


def autokey_encrypt(message, key_new):
    cipher_text = ''
    i = 0
    for letter in message:
        if letter == ' ':
            cipher_text += ' '
        else:
            x = (dict1[letter]+dict1[key_new[i]]) % 26
            i += 1
            cipher_text += dict2[x]
    return cipher_text

def autokey_decrypt(cipher_text, key_new):
    or_txt = ''
    i = 0
    for letter in cipher_text:
        if letter == ' ':
            or_txt += ' '
        else:
            x = (dict1[letter]-dict1[key_new[i]]+26) % 26
            i += 1
            or_txt += dict2[x]
    return or_txt


def main():
    text = input("Enter the text to encrypt/decrypt: ")
    while True:
            key = input("Enter the key for Autokey cipher: ")

            key = key.upper()
            text = text.upper()
            key = generate_auto_key(text, key)

            key = rail_fence_encrypt(key, 3)

            encrypted = autokey_encrypt(text, key)
            decrypted = autokey_decrypt(encrypted, key)
            print("Encrypted text:", encrypted)
            print("Decrypted text:", decrypted)


main()
