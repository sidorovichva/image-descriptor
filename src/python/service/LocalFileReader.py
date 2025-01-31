from PIL import Image

from src.python.service.FileReader import FileReader


class LocalFileReader(FileReader):

    def read(self, link: str) -> Image:
        image = Image.open(link)
        if image.mode != "RGB":
            image = image.convert(mode="RGB")
        return image
