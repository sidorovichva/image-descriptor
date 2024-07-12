import os


class Utils:

    @classmethod
    def is_directory_empty(cls, directory_path):
        return not any(os.scandir(directory_path))
