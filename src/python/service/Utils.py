import os


class Utils:

    @classmethod
    def is_directory_empty(cls, directory_path):
        return not any(os.scandir(directory_path))

    @classmethod
    def get_files_names_in_folder(cls, common_path):
        filenames = []
        for root, dirs, files in os.walk(common_path):
            for file in files:
                filenames.append(file)
        return filenames
