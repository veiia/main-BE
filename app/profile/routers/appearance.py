from fastapi import APIRouter, HTTPException

from app.profile.models import User
from app.profile.schemas import AppearanceSchema
from app.settings.tags import Tags

router = APIRouter(
    prefix=f"/{Tags.APPEARANCE}",
    tags=[Tags.PROFILE],
    # dependencies=[Depends(get_token_header)],
    responses={
        404: {"description": "Not found"},
        403: {"description": "Permission Denied"},
    },
)


@router.get("/", response_model=AppearanceSchema)
async def get_appearance(firstname: str) -> User:
    user = await User.objects.get_or_none(firstname=firstname)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    return user


@router.patch("/", response_model=AppearanceSchema)
async def change_appearance(firstname: str, appearance: AppearanceSchema) -> User:
    current = await User.objects.get_or_none(firstname=firstname)
    if not current:
        raise HTTPException(status_code=404, detail="Not found")
    return await current.update(**appearance.dict())
