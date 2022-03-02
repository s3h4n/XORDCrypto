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
                encrypted_data = self.xordc.encrypt(key, data)
                self.file.write_file(file_path, encrypted_data)
            elif option == "2":
                key_path = input("Key file: ")
                file_path = input("File to decrypt: ")
                key = self.file.read_file(key_path)
                data = self.file.read_file(file_path)
                decrypted_data = self.xordc.decrypt(key, data)
                self.file.write_file(file_path, decrypted_data)
            elif option == "3":
                key = self.xordc.generate_key(16)
                self.file.write_file("key.txt", key)
            elif option == "4":
                sys.exit()
            else:
                print("Invalid option")
