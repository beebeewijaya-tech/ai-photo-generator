from contextlib import asynccontextmanager
from functools import lru_cache

import uvicorn
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from db.conn import db
from routers.general import router as general_routes
from routers.image import router as image_routes
from routers.video import router as video_routes

templates = Jinja2Templates(directory="templates")


@lru_cache
def get_templates(req: Request):
    req.state.templates = templates
    return req


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.database.connect()
    yield

    await db.database.disconnect()


app = FastAPI(
    lifespan=lifespan,
    dependencies=[Depends(get_templates)]
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/ping")
async def ping():
    return "PONG!"


app.include_router(general_routes)
app.include_router(video_routes)
app.include_router(image_routes)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3000, reload=True)
