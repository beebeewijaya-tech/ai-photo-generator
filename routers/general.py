from fastapi import APIRouter, Request

router = APIRouter(
    tags=["General"]
)


@router.get("/")
async def home(req: Request):
    templates = req.state.templates
    return templates.TemplateResponse(
        request=req, name="home.html", context={"id": id}
    )
