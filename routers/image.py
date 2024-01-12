import datetime
from typing import List

from fastapi import APIRouter, HTTPException, UploadFile

from managers.auth import AuthManager
from managers.image import ImageManager

router = APIRouter(
    prefix="/image",
    tags=["Image"]
)


@router.post("/generate")
async def generate_image(files: List[UploadFile]):
    ip_addr = await AuthManager.get_api_info()
    get_ip_session = await AuthManager.get_session(ip_addr["ip"])
    if get_ip_session is None:
        data = {
            "ip_address": ip_addr["ip"],
            "usage": "1",
            "created_at": datetime.datetime.now()
        }
        await AuthManager.insert_session(data)
    else:
        usage = int(get_ip_session["usage"])
        if usage >= 3:
            raise HTTPException(400, "Already reach maximum limit, contact the administrator: beebeewijaya@gmail.com")
        usage += 1
        data = {
            "ip_address": ip_addr["ip"],
            "usage": f"{usage}",
        }
        await AuthManager.update_session(data)

    filename = ImageManager.upload_raw_photo(files)
    ai_photo = ImageManager.generate_ai_photo(filename)
    return ai_photo
