from fastapi import APIRouter

from app.settings.tags import Tags

projects_router = APIRouter(
    prefix=f"/{Tags.PROJECTS}",
    tags=[Tags.PROJECTS],
    # dependencies=[Depends(get_token_header)],
    responses={
        404: {"description": "Not found"},
        403: {"description": "Permission Denied"},
    },
)

projects_router.include_router(settings_router)
# projects_router.include_router()
# projects_router.include_router()
# projects_router.include_router()
