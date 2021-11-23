from fastapi import APIRouter

router = APIRouter()


@router.get("/", status_code=204)
def healthcheck() -> None:
    pass
