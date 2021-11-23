from fastapi import APIRouter

from .endpoints import healthcheck

api_router = APIRouter()
api_router.include_router(healthcheck.router, prefix="/healthcheck")
