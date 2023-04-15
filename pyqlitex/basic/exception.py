'''
    Exception Class
'''
class MetadataNotFoundError(Exception):
    """
    An exception that is raised when a metadata file does not contain a specified key.

    Attributes:
        file_type (str): The type of metadata file (e.g. "setup.cfg", "pyproject.toml").
        key (str): The name of the missing key.

    Methods:
        __str__(): Returns a string representation of the exception, 
            including the file type and key name.
    """

    def __init__(self, file_type: str, key: str) -> None:
        self.file_type = file_type
        self.key = key

    def __str__(self):
        return f"In file {self.file_type} found not key {self.key}"
