import ormar
import uvicorn
from fastapi import FastAPI

from app.profile.models import User
from app.profile.routers import router as router_profile
from app.settings.db import database

app = FastAPI()
app.state.database = database


@app.get('/', response_model=User)
async def index() -> User:
    try:
        return await User.objects.first()
    except ormar.exceptions.NoMatch:
        user, _ = await User.objects.get_or_create(email='test@test.com', firstname='name', lastname='name')
        return user


app.include_router(router_profile)


@app.on_event('startup')
async def startup() -> None:
    if not database.is_connected:
        await database.connect()
    # await init_db()
    # await User.objects.get_or_create(email='test@test.com')


@app.on_event('shutdown')
async def shutdown() -> None:
    if database.is_connected:
        await database.disconnect()


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level='info', reload=True)
