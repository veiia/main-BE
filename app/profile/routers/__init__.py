from fastapi import APIRouter

from app.profile.routers.appearance import router as router_appearance
from app.profile.routers.info import router as router_info
from app.settings.tags import Tags

router = APIRouter(
    prefix=f'/{Tags.PROFILE}',
    tags=[Tags.PROFILE],
    # dependencies=[Depends(get_token_header)],
    responses={
        404: {'description': 'Not found'},
        403: {'description': 'permission denied'},
    }
)

router.include_router(router_info)
router.include_router(router_appearance)
