from abc import ABC, abstractmethod

from PIL import Image

from src.python.enum.Algorithm import Algorithm


class Transformer(ABC):

    def __init__(self, short_name: Algorithm, name: str, folder: str):
        self.__short_name: Algorithm = short_name
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
    async def download(self) -> None:
        pass

    @abstractmethod
    def describe(self, image: Image) -> str:
        pass

    def path(self) -> str:
        return f"src/resources/transformers/{self.folder}"

    def model_path(self) -> str:
        return f"src/resources/transformers/{self.folder}/model"

    def processor_path(self) -> str:
        return f"src/resources/transformers/{self.folder}/processor"

    def feature_extractor_path(self) -> str:
        return f"src/resources/transformers/{self.folder}/feature_extractor"

    def auto_tokenizer_path(self) -> str:
        return f"src/resources/transformers/{self.folder}/auto_tokenizer"
