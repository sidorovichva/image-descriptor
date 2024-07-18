import os

import torch
from PIL.Image import Image

from src.python.enum.Algorithm import Algorithm
from src.python.service.Utils import Utils
from src.python.transformer.Transformer import Transformer
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, \
    AutoTokenizer


class NplConnectTransformer(Transformer):

    def __init__(self):
        super().__init__(
            short_name=Algorithm.nlpc,
            name='nlpconnect/vit-gpt2-image-captioning',
            folder='vit-gpt2-image-captioning'
        )

    async def download(self) -> None:
        if (
                not os.path.exists(self.path())
                or Utils.is_directory_empty(self.model_path())
                or Utils.is_directory_empty(self.feature_extractor_path())
                or Utils.is_directory_empty(self.auto_tokenizer_path())
        ):
            model = await VisionEncoderDecoderModel.from_pretrained(self.name)
            model.save_pretrained(self.model_path())

            feature_extractor = await ViTImageProcessor.from_pretrained(self.name)
            feature_extractor.save_pretrained(self.feature_extractor_path())

            tokenizer = await AutoTokenizer.from_pretrained(self.name)
            tokenizer.save_pretrained(self.auto_tokenizer_path())

    def describe(self, image: Image) -> str:
        model = VisionEncoderDecoderModel.from_pretrained(self.model_path())
        feature_extractor = ViTImageProcessor.from_pretrained(self.feature_extractor_path())
        tokenizer = AutoTokenizer.from_pretrained(self.auto_tokenizer_path())

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)

        pixel_values = feature_extractor(images=[image], return_tensors="pt").pixel_values
        pixel_values = pixel_values.to(device)

        max_length = 32
        num_beams = 8
        gen_kwargs = {"max_length": max_length, "num_beams": num_beams}
        output_ids = model.generate(pixel_values, **gen_kwargs)

        preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
        return [pred.strip() for pred in preds][0]
