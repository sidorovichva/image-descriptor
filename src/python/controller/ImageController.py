import os
from typing import Any, Dict, Coroutine, List

from fastapi import APIRouter

from src.python.enum.Algorithm import Algorithm
from src.python.factory.TransformerFactory import TransformerFactory
from src.python.service.ImageService import ImageService
from src.python.service.LocalFileReader import LocalFileReader
from src.python.service.Utils import Utils

router = APIRouter(prefix="/image")


@router.get("/describe")
async def describe(path: str, transformer_name: Algorithm = Algorithm.blip) -> Coroutine[Any, Any, dict[str, str]]:

    transformer = TransformerFactory.get_transformer(transformer_name=transformer_name)
    return ImageService(transformer).image2text(path)


@router.get("/test")
async def test(transformer_name: Algorithm) -> list[Coroutine[Any, Any, dict[str, str]]]:

    transformer = TransformerFactory.get_transformer(transformer_name=transformer_name)

    common_path: str = "src/resources/files/"

    files: [str] = Utils.get_files_names_in_folder(common_path)

    return [ImageService(transformer=transformer, file_reader=LocalFileReader()).image2text(path)
            for path in [common_path + file for file in files]]
