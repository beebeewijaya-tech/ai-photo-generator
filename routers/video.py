from fastapi import APIRouter, UploadFile

router = APIRouter(
    prefix="/video",
    tags=["Image"]
)


@router.post("/generate")
async def generate_subtitle(file: UploadFile):
    print(file)
