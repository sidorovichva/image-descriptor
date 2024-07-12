from src.python.transformer.BlipTransformer import BlipTransformer
from src.python.transformer.Transformer import Transformer


class TransformerFactory:

    @classmethod
    def get_transformer(cls, transformer_name: str) -> Transformer:
        match transformer_name:
            case "blip":
                return BlipTransformer()
            case _:
                raise ValueError(f"Unknown transformer name: {transformer_name}")