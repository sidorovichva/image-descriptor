import requests
from PIL import Image

from src.python.service.FileReader import FileReader


class RemoteFileReader(FileReader):

    def read(self, link: str) -> Image:
        image = Image.open(requests.get(link, stream=True).raw)
        if image.mode != "RGB":
            image = image.convert(mode="RGB")
        return image
