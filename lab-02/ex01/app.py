from flask import Flask, render_template, request

from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher

app = Flask(__name__)

# INIT
caesar = CaesarCipher()
vigenere = VigenereCipher()
rail = RailFenceCipher()
playfair = PlayFairCipher()
transposition = TranspositionCipher()

# HOME
@app.route("/")
def home():
    return render_template("index.html")

# ================= CAESAR =================
@app.route("/caesar")
def caesar_page():
    return render_template("caesar.html")

@app.route("/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    text = request.form["text"]
    key = int(request.form["key"])
    return caesar.encrypt_text(text, key)

@app.route("/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    text = request.form["text"]
    key = int(request.form["key"])
    return caesar.decrypt_text(text, key)

# ================= VIGENERE =================
@app.route("/vigenere")
def vigenere_page():
    return render_template("vigenere.html")

@app.route("/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    text = request.form["text"]
    key = request.form["key"]
    return vigenere.vigenere_encrypt(text, key)

@app.route("/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    text = request.form["text"]
    key = request.form["key"]
    return vigenere.vigenere_decrypt(text, key)

# ================= RAIL FENCE =================
@app.route("/railfence")
def rail_page():
    return render_template("railfence.html")

@app.route("/railfence/encrypt", methods=["POST"])
def rail_encrypt():
    text = request.form["text"]
    key = int(request.form["key"])
    return rail.rail_fence_encrypt(text, key)

@app.route("/railfence/decrypt", methods=["POST"])
def rail_decrypt():
    text = request.form["text"]
    key = int(request.form["key"])
    return rail.rail_fence_decrypt(text, key)

# ================= PLAYFAIR =================
@app.route("/playfair")
def playfair_page():
    return render_template("playfair.html")

@app.route("/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    text = request.form["text"]
    key = request.form["key"]
    matrix = playfair.create_playfair_matrix(key)
    return playfair.playfair_encrypt(text, matrix)

@app.route("/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    text = request.form["text"]
    key = request.form["key"]
    matrix = playfair.create_playfair_matrix(key)
    return playfair.playfair_decrypt(text, matrix)

# ================= TRANSPOSITION =================
@app.route("/transposition")
def transposition_page():
    return render_template("transposition.html")

@app.route("/transposition/encrypt", methods=["POST"])
def trans_encrypt():
    text = request.form["text"]
    key = int(request.form["key"])
    return transposition.encrypt(text, key)

@app.route("/transposition/decrypt", methods=["POST"])
def trans_decrypt():
    text = request.form["text"]
    key = int(request.form["key"])
    return transposition.decrypt(text, key)

# RUN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)