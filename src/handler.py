from ..packages import XORDCrypto
from ..packages import FileHelper


class Handler:
    def __init__(self) -> None:
        self.xordc = XORDCrypto()
        self.file = FileHelper()

    def handler(self) -> None:
        key = self.xordc.generate_key(16).decode()
        print("Key :", key)
        file_path = input("Enter the path to the file: ")
        original_data = self.file.read_file(file_path)
        print("Original data:", original_data)
        decrypted_data = self.xordc.decrypt(key, original_data)
        print("Encrypted data:", decrypted_data)
        self.file.write_file(file_path, decrypted_data)
