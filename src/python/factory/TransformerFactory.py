from src.python.enum.Algorithm import Algorithm
from src.python.transformer.BlipBaseTransformer import BlipBaseTransformer
from src.python.transformer.NplConnectTransformer import NplConnectTransformer
from src.python.transformer.Transformer import Transformer


class TransformerFactory:

    @classmethod
    def get_transformer(cls, transformer_name: str) -> Transformer:
        match transformer_name:
            case Algorithm.blip:
                return BlipBaseTransformer()
            case Algorithm.nlpc:
                return NplConnectTransformer()
            case _:
                raise ValueError(f"Unknown transformer name: {transformer_name}")