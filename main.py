from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from db import Base, engine
from routers import organizations, buildings, activities
from auth import verify_api_key
from settings import settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Directory API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Глобальная проверка API ключа
@app.middleware("http")
async def check_api_key(request: Request, call_next):
    if request.url.path.startswith("/docs") or request.url.path.startswith("/openapi.json"):
        return await call_next(request)
    api_key = request.headers.get("x-api-key")
    if api_key != settings.api_key:
        return JSONResponse(status_code=403, content={"detail": "Invalid API Key"})
    return await call_next(request)

# Кастомная OpenAPI-схема с security для x-api-key
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Directory API",
        version="1.0.0",
        description="Все запросы требуют заголовок `x-api-key`.",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "ApiKeyAuth": {
            "type": "apiKey",
            "in": "header",
            "name": "x-api-key"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", []).append({"ApiKeyAuth": []})
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi  # назначаем кастомную OpenAPI-функцию

app.include_router(organizations.router)
app.include_router(buildings.router)
app.include_router(activities.router)
