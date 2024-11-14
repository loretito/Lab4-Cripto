from Crypto.Cipher import AES, DES, DES3
from Crypto.Util.Padding import pad
import secrets
import base64

def print_message(m, size, key, new_key, type):
    adj = "se utilizará un random padding" if m == "menor" else "se truncará"

    print(f"{type} {m} al tamaño requerido ({size} bytes), {adj}.")
    print(f"{type} original:", key)
    print(f"{type} ajustada: {new_key}\n")


def adjust_key(key, size, type):
    if len(key) < size:
        random_padding = secrets.token_bytes(size - len(key))
        new_key = key + random_padding
        print_message("menor", size, key, new_key, type)

        return new_key
    
    elif len(key) > size:
        new_key = key[:size]
        print_message("mayor", size, key, new_key, type)

        return new_key
    
    return key


def encrypt(data, key, iv, algorithm="DES"):
    if algorithm == "AES":
        cipher = AES.new(key, AES.MODE_CBC, iv)
        cipher_text = cipher.encrypt(pad(data, AES.block_size))

    elif algorithm == "DES":
        cipher = DES.new(key, DES.MODE_CBC, iv)
        cipher_text = cipher.encrypt(pad(data, DES.block_size))

    elif algorithm == "3DES":
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        cipher_text = cipher.encrypt(pad(data, DES3.block_size))    

    else:
        raise ValueError("daf")
    
    encoded_cipher_text = base64.b64encode(cipher_text)
    return encoded_cipher_text.decode('utf-8')


def encrypt_and_print(data, key, iv, algorithm, key_size, iv_size):
    print(f"\n\033[33m== {algorithm} ==\033[0m")
    print(f"\033[34mTexto cifrado {algorithm}:\033[0m", encrypt(data, adjust_key(key, key_size, "Llave"), adjust_key(iv, iv_size, "IV"), algorithm))
