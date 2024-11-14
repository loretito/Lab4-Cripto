import secrets

from functions.encrypt_decrypt import encrypt, decrypt

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


def input_key_iv(type=""):
    key = input(f"Llave {type}: ").encode()
    iv = input(f"IV {type}: ").encode()

    return key, iv


def encrypt_and_print(data, key, iv, algorithm, key_size, iv_size):
    print(f"\n\033[33m== {algorithm} ==\033[0m")
    adj_key = adjust_key(key, key_size, "Llave")
    adj_IV = adjust_key(iv, iv_size, "IV")

    encoded_text = encrypt(data, adj_key, adj_IV, algorithm)
    print(f"\033[34mTexto cifrado {algorithm}:\033[0m", encoded_text)

    return encoded_text, adj_key, adj_IV


def decrypt_and_print(encoded_cipher_text, key, iv, algorithm, key_size, iv_size):
    print(f"\n\033[33m== {algorithm} (Descifrado) ==\033[0m")

    print(f"Texto cifrado: {encoded_cipher_text}")
    print(f"Llave: {key}")
    print(f"IV: {iv}\n")

    decrypted_text = decrypt(encoded_cipher_text, adjust_key(key, key_size, "Llave"), adjust_key(iv, iv_size, "IV"), algorithm)
    print(f"\033[34mTexto descifrado {algorithm}:\033[0m", decrypted_text) 