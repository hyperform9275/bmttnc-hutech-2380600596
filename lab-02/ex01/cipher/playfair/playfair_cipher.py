class PlayFairCipher:
    def __init__(self):
        self.matrix = []

    def create_playfair_matrix(self, key):
        key = key.upper().replace("J", "I")
        key = "".join(dict.fromkeys(key))

        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for char in key:
            alphabet = alphabet.replace(char, "")

        full_key = key + alphabet

        self.matrix = [list(full_key[i:i+5]) for i in range(0, 25, 5)]
        return self.matrix

    def find_letter_coords(self, matrix, letter):
        for r in range(5):
            for c in range(5):
                if matrix[r][c] == letter:
                    return r, c

    def prepare_text(self, text):
        text = text.upper().replace("J", "I").replace(" ", "")
        result = ""
        i = 0

        while i < len(text):
            a = text[i]
            b = ""

            if i + 1 < len(text):
                b = text[i + 1]

            if a == b or b == "":
                result += a + "X"
                i += 1
            else:
                result += a + b
                i += 2

        return result

    def playfair_encrypt(self, plain_text, matrix):
        plain_text = self.prepare_text(plain_text)
        encrypted_text = ""

        for i in range(0, len(plain_text), 2):
            a, b = plain_text[i], plain_text[i+1]

            r1, c1 = self.find_letter_coords(matrix, a)
            r2, c2 = self.find_letter_coords(matrix, b)

            if r1 == r2:
                encrypted_text += matrix[r1][(c1+1)%5]
                encrypted_text += matrix[r2][(c2+1)%5]
            elif c1 == c2:
                encrypted_text += matrix[(r1+1)%5][c1]
                encrypted_text += matrix[(r2+1)%5][c2]
            else:
                encrypted_text += matrix[r1][c2]
                encrypted_text += matrix[r2][c1]

        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper().replace(" ", "")
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            a, b = cipher_text[i], cipher_text[i+1]

            r1, c1 = self.find_letter_coords(matrix, a)
            r2, c2 = self.find_letter_coords(matrix, b)

            if r1 == r2:
                decrypted_text += matrix[r1][(c1-1)%5]
                decrypted_text += matrix[r2][(c2-1)%5]
            elif c1 == c2:
                decrypted_text += matrix[(r1-1)%5][c1]
                decrypted_text += matrix[(r2-1)%5][c2]
            else:
                decrypted_text += matrix[r1][c2]
                decrypted_text += matrix[r2][c1]

        return decrypted_text