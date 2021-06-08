def caesar_decrypt(plain_text, shift):
    if shift > 25:
        raise ValueError("shift < 26")
    else:
        alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        cipher_text = alphabets + alphabets
        return "".join(list(cipher_text[cipher_text.index(t) + shift] if t != ' ' else ' ' for idx, t in enumerate(plain_text)))


for idx in range(26):
    cipher_text = caesar_decrypt("CNMS FDS GTQS", idx)
    print(cipher_text)
