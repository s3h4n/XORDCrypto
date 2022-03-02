import base64
import random
import sys


class XORDCrypto:
    @staticmethod
    def generate_key(size: int) -> bytes:
        """
        generate_key will generate a random key of the specified size.

        :param size: The size of the key to generate.
        :type size: int
        :return: The generated key.
        :rtype: bytes
        """
        try:
            return base64.b64encode(bytes(random.randbytes(size)))
        except Exception as e:
            print("Error in XORDCrypto.generate_key()\n>>>", e)
            sys.exit(1)

    @staticmethod
    def convert(key: bytes, data: bytes) -> bytes:
        """
        convert will convert the data using the specified key.

        :param key: The key to use for conversion.
        :type key: bytes
        :param data: The data to convert.
        :type data: bytes
        :return: The converted data.
        :rtype: bytes
        """
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
