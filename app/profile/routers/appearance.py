from fastapi import APIRouter

from app.settings.tags import Tags

router = APIRouter(
    prefix=f'/{Tags.APPEARANCE}',
    tags=[Tags.PROFILE],
    # dependencies=[Depends(get_token_header)],
    responses={
        404: {'description': 'Not found'},
        403: {'description': 'permission denied'},
    }
)


@router.get('/')
async def get_appearance():
    return {'name': 'appearance get'}


@router.patch('/')
async def change_appearance():
    return {'name': 'appearance patch'}