from fastapi import APIRouter

from settings.tags import Tags

settings_router = APIRouter(
    prefix=f"/{Tags.SETTINGS}",
    # tags=[Tags.PROJECTS],
    # dependencies=[Depends(get_token_header)],
    responses={
        404: {"description": "Not found"},
        403: {"description": "Permission Denied"},
    },
)


@settings_router.get("/user/{user_id}/{activity_id}", response_model=ActivityUserResponse)
async def get_user_activity(user_id: str, activity_id: str):
    user_activity = await UserActivity.objects.filter(
        user=user_id, id=activity_id
    ).first()
    return user_activity
