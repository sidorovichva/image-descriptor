import requests
from PIL import Image

from src.python.service.FileReader import FileReader


class RemoteFileReader(FileReader):

    def read(self, link: str) -> Image:
        return Image.open(requests.get(link, stream=True).raw).convert('RGB')
