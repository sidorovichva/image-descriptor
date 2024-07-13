from PIL import Image

from src.python.service.FileReader import FileReader
from src.python.service.RemoteFileReader import RemoteFileReader
from src.python.transformer.Transformer import Transformer


class ImageService:

    def __init__(self, transformer: Transformer, file_reader: FileReader = RemoteFileReader()):
        self.__transformer = transformer
        self.__file_reader = file_reader

    @property
    def transformer(self) -> Transformer:
        return self.__transformer

    @property
    def file_reader(self) -> FileReader:
        return self.__file_reader

    def image2text(self, path: str) -> dict:

        self.transformer.download()

        image: Image = self.file_reader.read(path)

        description: str = self.transformer.describe(image)

        return {path: description}
