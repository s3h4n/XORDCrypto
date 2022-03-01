import base64
import random
import sys


class XORDCrypto:
    """
    This is the helper class for encryption using XOR approach.
    """

    @staticmethod
    def generate_key(size: int) -> bytes:
        """
        generate_key will generate an encryption key.

        :param size: Size of the key(bytes)
        :type size: int
        :return: Encryption key.
        :rtype: str
        """
        try:
            return base64.b64encode(bytes(random.randbytes(size)))
        except Exception as e:
            print("Error in XORDCrypto.generate_key()\n>>>", e)
            sys.exit(1)

    @staticmethod
    def converter(key: str, string: str) -> str:
        """
        converter will convert the string to bytes and then XOR it with the key.

        :param key: Encryption key.
        :type key: str
        :param string: String to be encrypted/decrypted.
        :type string: str
        :return: Encrypted/Decrypted string.
        :rtype: str
        """
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
        """
        encrypt will encrypt the string using XOR and base64.

        :param key: Encryption key.
        :type key: str
        :param string: String to be encrypted.
        :type string: str
        :return: Encrypted string.
        :rtype: bytes
        """
        try:
            output = self.converter(key, string)
            return base64.b64encode(output.encode())
        except Exception as e:
            print("Error in XORDCrypto.encrypt()\n>>>", e)
            sys.exit(1)

    def decrypt(self, key: str, string: bytes) -> str:
        """
        decrypt will decrypt the string using XOR and base64.

        :param key: Encryption key.
        :type key: str
        :param string: String to be decrypted.
        :type string: bytes
        :return: Decrypted string.
        :rtype: str
        """
        try:
            output = base64.b64decode(string).decode()
            return self.converter(key, output)
        except Exception as e:
            print("Error in XORDCrypto.encrypt()\n>>>", e)
            sys.exit(1)
