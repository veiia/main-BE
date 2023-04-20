from fastapi import APIRouter

from activity.models import ContainerActivity, UserActivity
from activity.responses import (
    ActivityContainerResponse,
    ActivityUserResponse,
    ListActivityContainerResponse,
    ListActivityUserResponse,
)
from app.settings.tags import Tags

router = APIRouter(
    prefix=f"/{Tags.ACTIVITY}",
    tags=[Tags.ACTIVITY],
    # dependencies=[Depends(get_token_header)],
    responses={
        404: {"description": "Not found"},
        403: {"description": "Permission Denied"},
    },
)


@router.get("/user/{user_id}/{activity_id}", response_model=ActivityUserResponse)
async def get_user_activity(user_id: str, activity_id: str):
    user_activity = await UserActivity.objects.filter(
        user=user_id, id=activity_id
    ).first()
    return user_activity


@router.get("/user/{user_id}", response_model=ListActivityUserResponse)
async def get_user_list_of_activity(user_id: str):
    user_activities = await UserActivity.objects.filter(user=user_id).all()
    return user_activities


@router.patch("/containers", response_model=ListActivityContainerResponse)
async def get_container_activity(user_id: str) -> ListActivityContainerResponse:
    # TODO: pagination limit and offset
    containers_activity = await ContainerActivity.objects.filter(user=user_id).all()
    return containers_activity


@router.patch("/containers/{container_id}", response_model=ActivityContainerResponse)
async def get_container_list_of_activity(
    user_id: str, container_id: str
) -> ActivityContainerResponse:
    container_activities = await ContainerActivity.objects.filter(
        user=user_id, id=container_id
    ).all()
    return container_activities
