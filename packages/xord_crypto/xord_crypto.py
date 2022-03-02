import base64
import random
import sys


class XORDCrypto:
    @staticmethod
    def generate_key(size: int) -> bytes:
        try:
            return base64.b64encode(bytes(random.randbytes(size)))
        except Exception as e:
            print("Error in XORDCrypto.generate_key()\n>>>", e)
            sys.exit(1)

    @staticmethod
    def converter(key: str, string: str) -> str:
        output = ""
        try:
            for i in range(len(string)):
                j = i % len(key)
                output += chr(ord(string[i]) ^ ord(key[j]))
            return output
        except Exception as e:
            print("Error in XORDCrypto.converter()\n>>>", e)
            sys.exit(1)

    def encrypt(self, key: str, string: str) -> bytes:
        try:
            output = self.converter(key, string)
            return base64.b64encode(output.encode())
        except Exception as e:
            print("Error in XORDCrypto.encrypt()\n>>>", e)
            sys.exit(1)

    def decrypt(self, key: str, string: bytes) -> bytes:
        try:
            output = base64.b64decode(string).decode()
            return self.converter(key, output).encode()
        except Exception as e:
            print("Error in XORDCrypto.encrypt()\n>>>", e)
            sys.exit(1)
