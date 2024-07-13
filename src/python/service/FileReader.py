from abc import ABC, abstractmethod

from PIL import Image


class FileReader(ABC):

    @abstractmethod
    def read(self, link: str) -> Image:
        pass
