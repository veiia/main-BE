from fastapi import APIRouter, HTTPException

from app.profile.models import User
from app.profile.schemas import UserOut, UserUpdate
from app.settings.tags import Tags

router = APIRouter(
    prefix=f"/{Tags.ME}",
    tags=[Tags.PROFILE],
    # dependencies=[Depends(get_token_header)],
    responses={
        404: {"description": "Not found"},
        403: {"description": "Permission Denied"},
    },
)


@router.get("/", response_model=UserOut)
async def get_profile_information(firstname: str) -> User:
    user = await User.objects.get_or_none(firstname=firstname)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    return user


@router.patch("/", response_model=UserOut)
async def edit_profile_information(firstname: str, user: UserUpdate) -> User:
    current = await User.objects.get_or_none(firstname=firstname)
    if not current:
        raise HTTPException(status_code=404, detail="Not found")
    return await current.update(**user.dict())


@router.delete("/")
async def delete_profile(firstname: str) -> None:
    user = await User.objects.get_or_none(firstname=firstname)
    if not user:
        raise HTTPException(status_code=404, detail="Not found")
    await user.delete()
    raise HTTPException(status_code=204, detail="Item deleted successfully")
