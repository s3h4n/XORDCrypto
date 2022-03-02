import sys


class FileHelper:
    """
    This class is used to read and write files.
    """

    @staticmethod
    def read_file(file_path: str) -> str:
        """
        read_file reads a file and returns its content as a bytes object.

        :param file_path: the path to the file.
        :type file_path: str
        :return: the content of the file.
        :rtype: str
        """
        try:
            with open(file_path, "rb") as file:
                return file.read()
        except Exception as e:
            print("Error in FileHelper.read_file()\n>>>", e)
            sys.exit(1)

    @staticmethod
    def write_file(file_path: str, data: str) -> None:
        """
        write_file writes data to a file.

        :param file_path: the path to the file.
        :type file_path: str
        :param data: the data to write to the file.
        :type data: str
        """
        try:
            with open(file_path, "wb") as file:
                file.write(data)
        except Exception as e:
            print("Error in FileHelper.write_file()\n>>>", e)
            sys.exit(1)
