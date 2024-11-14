from Crypto.Cipher import AES, DES, DES3
from Crypto.Util.Padding import pad, unpad
import base64


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
        raise ValueError("Opción no válida.")
    
    encoded_cipher_text = base64.b64encode(cipher_text)
    return encoded_cipher_text.decode('utf-8')


def decrypt(encoded_cipher_text, key, iv, algorithm="DES"):
    cipher_text = base64.b64decode(encoded_cipher_text)
    
    if algorithm == "AES":
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(cipher_text), AES.block_size)
        
    elif algorithm == "DES":
        cipher = DES.new(key, DES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(cipher_text), DES.block_size)
        
    elif algorithm == "3DES":
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(cipher_text), DES3.block_size)
        
    else:
        raise ValueError("Algoritmo no soportado")
    
    return decrypted_data.decode('utf-8')