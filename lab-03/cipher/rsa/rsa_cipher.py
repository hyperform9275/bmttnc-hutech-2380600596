from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import os


class RSACipher:
    def __init__(self):
        self.key_folder = "cipher/rsa/keys"
        os.makedirs(self.key_folder, exist_ok=True)

    def generate_keys(self):
        key = RSA.generate(2048)

        with open(os.path.join(self.key_folder, "privatekey.pem"), "wb") as f:
            f.write(key.export_key())

        with open(os.path.join(self.key_folder, "publickey.pem"), "wb") as f:
            f.write(key.publickey().export_key())

    def load_keys(self):
        with open(os.path.join(self.key_folder, "privatekey.pem"), "rb") as f:
            private_key = RSA.import_key(f.read())

        with open(os.path.join(self.key_folder, "publickey.pem"), "rb") as f:
            public_key = RSA.import_key(f.read())

        return private_key, public_key

    def encrypt(self, message, key):
        cipher = PKCS1_OAEP.new(key)
        return cipher.encrypt(message.encode("utf-8"))

    def decrypt(self, ciphertext, key):
        cipher = PKCS1_OAEP.new(key)
        return cipher.decrypt(ciphertext).decode("utf-8")

    def sign(self, message, key):
        h = SHA256.new(message.encode("utf-8"))
        return pkcs1_15.new(key).sign(h)

    def verify(self, message, signature, key):
        h = SHA256.new(message.encode("utf-8"))
        try:
            pkcs1_15.new(key).verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False