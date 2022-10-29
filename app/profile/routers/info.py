from fastapi import APIRouter

from app.settings.tags import Tags

router = APIRouter(
    prefix=f"/{Tags.ME}",
    tags=[Tags.PROFILE],
    # dependencies=[Depends(get_token_header)],
    responses={
        404: {"description": "Not found"},
        403: {"description": "permission denied"},
    },
)


@router.get("/")
async def get_profile_information():
    return {"name": "me get"}


@router.patch("/")
async def edit_profile_information():
    return {"name": "me patch"}


@router.delete("/")
async def delete_profile():
    return {"name": "me delete"}
