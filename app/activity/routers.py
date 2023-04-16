from fastapi import APIRouter, HTTPException

from activity.models import Activity
from activity.responses import ListActivityContainerResponse, ListActivityUserResponse
from app.settings.tags import Tags

router = APIRouter(
    prefix=f'/{Tags.ACTIVITY}',
    tags=[Tags.ACTIVITY],
    # dependencies=[Depends(get_token_header)],
    responses={
        404: {'description': 'Not found'},
        403: {'description': 'Permission Denied'},
    },
)


@router.get('/containers/logs', response_model=ListActivityContainerResponse)
async def get_usage(usage_id: str):
    pass


@router.patch('/user/logs', response_model=ListActivityUserResponse)
async def get_usage_list(user_id: str) -> Activity:
    # TODO: pagination
    user_activity = await Activity.objects.filter(user=user_id).all()
    return user_activity
