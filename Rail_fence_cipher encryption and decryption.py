def encrypt_rail_fence(text, rails):
    # Create an empty matrix to store the rail fence pattern
    matrix = [['' for _ in range(len(text))] for _ in range(rails)]

    # Populate the matrix with characters from the text
    row, direction = 0, 1
    for char in text:
        matrix[row][0] += char
        row += direction
        if row == rails or row == -1:
            direction *= -1
            row += 2 * direction

    # Concatenate rows to get the encrypted text
    encrypted_text = ''.join([''.join(row) for row in matrix])

    return encrypted_text

def decrypt_rail_fence(text, rails):
    # Create an empty matrix to store the rail fence pattern
    matrix = [['' for _ in range(len(text))] for _ in range(rails)]

    # Initialize variables for matrix filling
    index = 0
    row, direction = 0, 1

    # Fill the matrix with the structure of the rail fence
    for j in range(len(text)):
        matrix[row][j] = '.'
        row += direction
        if row == rails or row == -1:
            direction *= -1
            row += 2 * direction

    # Fill the matrix with the encrypted text
    for i in range(rails):
        for j in range(len(text)):
            if matrix[i][j] == '.':
                matrix[i][j] = text[index]
                index += 1

    # Read the matrix in zigzag pattern to get the decrypted text
    decrypted_text = ''
    row, direction = 0, 1
    for j in range(len(text)):
        decrypted_text += matrix[row][j]
        row += direction
        if row == rails or row == -1:
            direction *= -1
            row += 2 * direction

    return decrypted_text

# Example usage:
text_to_encrypt = "COMPUTER SCIENCE AND ENGINEERING"
rails = 3

encrypted_text = encrypt_rail_fence(text_to_encrypt, rails)
print("Encrypted:", encrypted_text)

decrypted_text = decrypt_rail_fence(encrypted_text, rails)
print("Decrypted:", decrypted_text)
