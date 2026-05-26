from fastapi import APIRouter

# v1 라우터 (기존 호환)
v1_router = APIRouter(prefix="/api/v1", tags=["v1"])

# v2 라우터 (신규)
v2_router = APIRouter(prefix="/api/v2", tags=["v2"])

def create_versioned_app(app):
    app.include_router(v1_router)
    app.include_router(v2_router)

    @app.get("/api/version")
    def get_api_version():
        return {
            "latest": "v2",
            "supported": ["v1", "v2"],
            "deprecated": {
                "v1": {"sunset_date": "2025-12-31", "migration_guide": "/docs/v1-to-v2"}
            }
        }
