from fastapi import APIRouter, HTTPException

from app.settings.tags import Tags
from usage.models import Usage
from usage.responses import ListUsageResponse, UsageResponse

router = APIRouter(
    prefix=f"/{Tags.USAGE}",
    tags=[Tags.USAGE],
    # dependencies=[Depends(get_token_header)],
    responses={
        404: {"description": "Not found"},
        403: {"description": "Permission Denied"},
    },
)


@router.get("/{usage_id}", response_model=UsageResponse)
async def get_usage(usage_id: str) -> Usage:
    user = await Usage.objects.get_or_none(id=usage_id)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    return user


@router.patch("/", response_model=ListUsageResponse)
async def get_usage_list(user_id: str) -> None:
    feedbacks = await Usage.objects.filter(user=user_id).all()
    return feedbacks
