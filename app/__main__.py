import uvicorn
from fastapi import FastAPI

from app.settings.db import database, User
from app.profile.routers import router as router_profile

app = FastAPI()
app.state.database = database


@app.get('/')
async def index():
    users = await User.objects.all()
    return {'message': users}

app.include_router(router_profile)


@app.on_event('startup')
async def startup() -> None:
    if not database.is_connected:
        await database.connect()
    await User.objects.get_or_create(email='test@test.com')


@app.on_event('shutdown')
async def shutdown() -> None:
    if database.is_connected:
        await database.disconnect()


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000, log_level="info", reload=True)
