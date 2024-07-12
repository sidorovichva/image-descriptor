from fastapi import APIRouter

from src.python.factory.TransformerFactory import TransformerFactory
from src.python.service.ImageService import ImageService

router = APIRouter(prefix="/image")


@router.get("/describe")
async def describe(path: str, transformer_name: str) -> str:

    transformer = TransformerFactory.get_transformer(transformer_name=transformer_name)
    return ImageService(transformer).describe(path)
