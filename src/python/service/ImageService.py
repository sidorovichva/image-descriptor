from PIL import Image
from transformers import BlipForConditionalGeneration, BlipProcessor
import os

from src.python.service.FileReader import FileReader
from src.python.service.RemoteFileReader import RemoteFileReader
from src.python.transformer.Transformer import Transformer
from src.python.service.Utils import Utils


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

    def describe(self, path: str) -> dict:

        local_model_path: str = self.transformer.model_path()
        local_processor_path: str = self.transformer.processor_path()

        if (
                not os.path.exists(self.transformer.path())
                or Utils.is_directory_empty(local_model_path)
                or Utils.is_directory_empty(local_processor_path)
        ):
            self.transformer.download()

        processor = BlipProcessor.from_pretrained(local_processor_path)
        model = BlipForConditionalGeneration.from_pretrained(local_model_path)
        raw_image = self.file_reader.read(path)
        inputs = processor(raw_image, return_tensors="pt")
        out = model.generate(**inputs)

        return {path: processor.decode(out[0], skip_special_tokens=True)}
