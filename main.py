from functions.utils import adjust_key, encrypt

print("Utilizar la misma llave/IV para todos los algoritmos? (s/n)")
while True:
    option = input("s/n: ").lower()
    if option in ["s", "n"]:
        break
    print("Opción no válida.")


def encrypt_and_print(data, key, iv, algorithm, key_size, iv_size):
    print(f"\n\033[33m== {algorithm} ==\033[0m")
    print(f"\033[34mTexto cifrado {algorithm}:\033[0m", encrypt(data, adjust_key(key, key_size, "Llave"), adjust_key(iv, iv_size, "IV"), algorithm))


data = input("Texto a encriptar: ").encode()

if option == "s":
    key = input("Llave: ").encode()
    iv = input("IV: ").encode()

    print("\n\033[34mTexto original:\033[0m", data)
    encrypt_and_print(data, key, iv, "AES", 32, 16)
    encrypt_and_print(data, key, iv, "DES", 8, 8)
    encrypt_and_print(data, key, iv, "3DES", 24, 8)

else: 
    key_aes = input("Llave AES: ").encode()
    iv_aes = input("IV AES: ").encode()
    key_des = input("Llave DES: ").encode()
    iv_des = input("IV DES: ").encode()
    key_3des = input("Llave 3DES: ").encode()
    iv_3des = input("IV 3DES: ").encode()

    print("\n\033[34mTexto original:\033[0m", data)
    encrypt_and_print(data, key_aes, iv_aes, "AES", 32, 16)
    encrypt_and_print(data, key_des, iv_des, "DES", 8, 8)
    encrypt_and_print(data, key_3des, iv_3des, "3DES", 24, 8)
