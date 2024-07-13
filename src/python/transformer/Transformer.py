from abc import ABC, abstractmethod


class Transformer(ABC):

    def __init__(self, short_name: str, name: str, folder: str):
        self.__short_name: str = short_name
        self.__name: str = name
        self.__folder: str = folder

    @property
    def short_name(self) -> str:
        return self.__short_name

    @property
    def name(self) -> str:
        return self.__name

    @property
    def folder(self) -> str:
        return self.__folder

    @abstractmethod
    def download(self) -> None:
        pass

    def path(self) -> str:
        return f"src/resources/transformers/{self.folder}"

    def model_path(self) -> str:
        return f"src/resources/transformers/{self.folder}/model"

    def processor_path(self) -> str:
        return f"src/resources/transformers/{self.folder}/processor"
