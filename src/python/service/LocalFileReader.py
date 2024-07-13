import requests
from PIL import Image

from src.python.service.FileReader import FileReader


class LocalFileReader(FileReader):

    def read(self, link: str) -> Image:
        return Image.open(link).convert('RGB')
