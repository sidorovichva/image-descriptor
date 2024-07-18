import os

from PIL import Image

from src.python.enum.Algorithm import Algorithm
from src.python.service.Utils import Utils
from src.python.transformer.Transformer import Transformer
from transformers import BlipForConditionalGeneration, BlipProcessor


class BlipBaseTransformer(Transformer):

    def __init__(self):
        super().__init__(
            short_name=Algorithm.blip,
            name='Salesforce/blip-image-captioning-base',
            folder='blip-image-captioning-base'
        )

    async def download(self) -> None:
        if (
                not os.path.exists(self.path())
                or Utils.is_directory_empty(self.model_path())
                or Utils.is_directory_empty(self.processor_path())
        ):
            processor = await BlipProcessor.from_pretrained(self.name)
            processor.save_pretrained(self.processor_path())

            model = await BlipForConditionalGeneration.from_pretrained(self.name)
            model.save_pretrained(self.model_path())

    def describe(self, image: Image) -> str:
        processor = BlipProcessor.from_pretrained(self.processor_path())
        model = BlipForConditionalGeneration.from_pretrained(self.model_path())
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs, max_new_tokens=512)
        return processor.decode(out[0], skip_special_tokens=True)
