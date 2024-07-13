from fastapi import APIRouter

from src.python.factory.TransformerFactory import TransformerFactory
from src.python.service.ImageService import ImageService
from src.python.service.LocalFileReader import LocalFileReader

router = APIRouter(prefix="/image")


@router.get("/describe")
async def describe(path: str, transformer_name: str) -> dict:

    transformer = TransformerFactory.get_transformer(transformer_name=transformer_name)
    return ImageService(transformer).describe(path)


@router.get("/test")
async def describe(transformer_name: str) -> list[dict]:

    transformer = TransformerFactory.get_transformer(transformer_name=transformer_name)

    common_path: str = "src/resources/files/"

    files = [
        'circles.jpg',
        'diffuser.png',
        'floor_plan.png',
        'general_notes.png',
        'icon.jpg',
        'image1.jpg',
        'image2.jpg',
        'image3.jpg',
        'mixed_shapes_0.jpg',
        'mixed_shapes_1.jpg',
        'schedule.png',
        'Screenshot 1.png',
        'Screenshot 2.png',
    ]

    return [ImageService(transformer=transformer, file_reader=LocalFileReader()).describe(path)
            for path in [common_path + file for file in files]]
