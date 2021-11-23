import sentry_sdk
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from api.v1.router import api_router
from core.config import settings


app = FastAPI(title=settings.PROJECT_NAME, openapi_url="/v1/openapi.json")

if settings.SENTRY_DSN:
    sentry_sdk.init(dsn=settings.SENTRY_DSN)
    app.add_middleware(SentryAsgiMiddleware)

app.include_router(api_router, prefix="/v1")
