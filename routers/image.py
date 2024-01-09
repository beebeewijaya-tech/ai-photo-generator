from typing import List

from fastapi import APIRouter, UploadFile

from managers.image import ImageManager

router = APIRouter(
    prefix="/image",
    tags=["Image"]
)


@router.post("/generate")
async def generate_image(files: List[UploadFile]):
    filename = ImageManager.upload_raw_photo(files)
    ai_photo = ImageManager.generate_ai_photo(filename)
    return ai_photo
