import os


class PathCheck:
    """
    Creates a valid Path Check controller which provides a consistent path
    """
    def __init__(self, path: str, is_dir: bool = False):
        self.is_dir = is_dir
        self.__path = self.__get_valid_path(path)

    def __get_valid_path(self, i_path: str) -> os.path:
        """
        Checks if a file path exists or not, and returns a valid filepath

        Args:
            path (str): Path to check

        Returns:
            os.path: Valid filepath (according to os.path standards)
        """
        if not os.path.exists(i_path):
            if self.is_dir:
                os.makedirs(i_path)
        
        return os.path.abspath(i_path)
    
    def GetPath(self) -> os.path:
        """
        Provides a failchecked file path

        Returns:
            os.path: Failchecked FilePath
        """
        return self.__path
    