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
    def convert(key: bytes, data: bytes) -> str:
        key = bytearray(key)
        data = bytearray(data)
        try:
            for index, values in enumerate(data):
                x = index % len(key)
                data[index] = values ^ x
            return data
        except Exception as e:
            print("Error in XORDCrypto.converter()\n>>>", e)
            sys.exit(1)
