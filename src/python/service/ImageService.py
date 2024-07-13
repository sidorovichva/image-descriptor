from PIL import Image
from transformers import BlipForConditionalGeneration, BlipProcessor
import os

from src.python.transformer.Transformer import Transformer
from src.python.service.Utils import Utils


class ImageService:

    def __init__(self, transformer: Transformer):
        self.__transformer = transformer

    @property
    def transformer(self):
        return self.__transformer

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
        raw_image = Image.open(path).convert('RGB')
        inputs = processor(raw_image, return_tensors="pt")
        out = model.generate(**inputs)

        return {path.split('/')[-1]: processor.decode(out[0], skip_special_tokens=True)}
