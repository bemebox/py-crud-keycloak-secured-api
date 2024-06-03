from fastapi import APIRouter

router = APIRouter()
health_tags_metadata = {
    "name": "health",
    "description": "API health check operations.",
}


@router.get("/health", status_code=200)
def health_check():
    return {"status": "ok"}
