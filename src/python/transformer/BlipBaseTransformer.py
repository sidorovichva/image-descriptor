from src.python.enum.Algorithm import Algorithm
from src.python.transformer.Transformer import Transformer
from transformers import BlipForConditionalGeneration, BlipProcessor


class BlipBaseTransformer(Transformer):

    def __init__(self):
        super().__init__(
            short_name=Algorithm.blip,
            name='Salesforce/blip-image-captioning-base',
            folder='blip-image-captioning-base'
        )

    def download(self) -> None:
        processor = BlipProcessor.from_pretrained(self.name)
        processor.save_pretrained(self.processor_path())

        model = BlipForConditionalGeneration.from_pretrained(self.name)
        model.save_pretrained(self.model_path())
