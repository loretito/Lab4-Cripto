from functions.utils import encrypt_and_print, decrypt_and_print, input_key_iv

def process_data(option, data):
    algorithms = [
        ("AES", 32, 16),
        ("DES", 8, 8),
        ("3DES", 24, 8)
    ]

    encrypted_data = []
    
    if option == "s":
        key, iv = input_key_iv("Todos los algoritmos")
        
        print("\n\033[35m\n === CIFRADO ===\033[0m\n")
        print("\n\033[34mTexto original:\033[0m", data)
        
        for algorithm, key_size, iv_size in algorithms:
            encrypted, key_out, iv_out = encrypt_and_print(data, key, iv, algorithm, key_size, iv_size)
            encrypted_data.append((encrypted, key_out, iv_out, algorithm, key_size, iv_size))

    else:
        print("\n\033[35m\n === CIFRADO ===\033[0m\n")
        print(f"\n\033[34mTexto original:\033[0m {data}")
        
        for algorithm, key_size, iv_size in algorithms:
            key, iv = input_key_iv(algorithm)
            encrypted, key_out, iv_out = encrypt_and_print(data, key, iv, algorithm, key_size, iv_size)
            encrypted_data.append((encrypted, key_out, iv_out, algorithm, key_size, iv_size))

    print("\n\033[35m\n === DESCIFRADO ===\033[0m\n")
    for encrypted, key_out, iv_out, algorithm, key_size, iv_size in encrypted_data:
        decrypt_and_print(encrypted, key_out, iv_out, algorithm, key_size, iv_size)

def main():
    print("\n\033[35m=== CIFRADO Y DESCIFRADO (AES/DES/3DES) ===\033[0m\n\n")

    print("Utilizar la misma llave/IV para todos los algoritmos? (s/n)")
    while True:
        option = input("s/n: ").lower()
        if option in ["s", "n"]:
            break
        print("❌ Opción no válida.\n")

    data = input("\nTexto a encriptar: ").encode()
    process_data(option, data)

if __name__ == "__main__":
    main()
