from ..packages import XORDCrypto
from ..packages import FileHelper
from . import constants
from subprocess import call
import sys


class Handler:
    def __init__(self) -> None:
        """
        __init__ is the constructor for the Handler class.
        """
        self.xordc = XORDCrypto()
        self.file = FileHelper()
        self.b = constants.COLOR["bold"]
        self.e = constants.COLOR["end"]

    def handler(self) -> None:
        """
        handler for the CLI interface of the program.
        """

        message = ""

        while True:
            call(["clear"])  # clear the screen
            print(message)
            print(f"\n{self.b}Welcome to XORDCrypto!{self.e} 🔑\n")

            # print the options
            for item in constants.MENU:
                print(f"{item}")

            choice = input(f"\n{self.b}Choose an option: {self.e}")

            # check choices
            if choice == "1":

                key_path = input(f"\n{self.b}Key file: {self.e}") or None
                file_path = (
                    input(f"\n{self.b}File to Encrypt/Decrypt: {self.e}") or None
                )
                key = self.file.read_file(key_path)
                data = self.file.read_file(file_path)
                print(f"\n{self.b}Converting...{self.e}\n")
                output = self.xordc.convert(key, data)
                self.file.write_file(file_path, output)
                message = f"\n{self.b}Successfully converted the file!{self.e}"

            elif choice == "2":

                key = self.xordc.generate_key(32)
                print(f"\n{self.b}Key:{self.e}{key}")
                key_path = (
                    input(f"\n{self.b}Save key to file [ex : sample.key]: {self.e}")
                    or "sample.key"
                )
                self.file.write_file(key_path, key)
                message = f"\nSuccessfull! Key saved in {key_path}"

            elif choice == "3":

                print(f"\n{self.b}Exiting...{self.e}")
                sys.exit(0)

            else:

                print(f"\n{self.b}Invalid choice!{self.e}")
