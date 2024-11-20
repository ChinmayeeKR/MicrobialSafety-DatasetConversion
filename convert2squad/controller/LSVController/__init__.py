from typing import List

class LSVController:
    """
    A controller to ingest a text file with line-separated values and 
    provide its contents as a list of strings.
    """

    def __init__(self, filepath: str):
        """
        Initializes the LSVController with the file path.

        Args:
            filepath (str): The path to the text file containing line-separated values.
        """
        self.filepath = filepath
        self._lines = []
        self.__ingest()

    def __ingest(self):
        """
        Reads the file and stores its contents as a list of strings.

        Raises:
            FileNotFoundError: If the specified file does not exist.
            Exception: If any other error occurs while reading the file.
        """
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                self._lines = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{self.filepath}' was not found.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the file: {e}")

    def to_list_of_str(self) -> List[str]:
        """
        Returns the list of strings obtained from the file.

        Returns:
            List[str]: A list of strings, where each string corresponds to a line in the file.
        """
        return self._lines
