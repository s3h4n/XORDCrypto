import sys
from ..packages import XORDCrypto
from ..packages import FileHelper


class Handler:
    def __init__(self) -> None:
        self.xordc = XORDCrypto()
        self.file = FileHelper()

    def handler(self) -> None:
        while True:
            print("Select an option:")
            print("1. Encrypt")
            print("2. Decrypt")
            print("3. Generate key")
            print("4. Exit")
            option = input("Option: ")
            if option == "1":
                key_path = input("Key file: ")
                file_path = input("File to encrypt: ")
                key = self.file.read_file(key_path)
                data = self.file.read_file(file_path)
                encrypted_data = self.xordc.convert(key, data)
                self.file.write_file(file_path, encrypted_data)
            elif option == "2":
                key_path = input("Key file: ")
                file_path = input("File to decrypt: ")
                key = self.file.read_file(key_path)
                data = self.file.read_file(file_path)
                decrypted_data = self.xordc.convert(key, data)
                self.file.write_file(file_path, decrypted_data)
            elif option == "3":
                key = self.xordc.generate_key(32)
                print(f"Your key is `{key}`.\nSaved to the `key.key`.")
                self.file.write_file("key.key", key)
            elif option == "4":
                sys.exit()
            else:
                print("Invalid option")
