from fastapi import FastAPI

from app.settings.db import database, User

app = FastAPI()
app.state.database = database


@app.get('/')
async def main():
    users = await User.objects.all()
    return {'message': users}


@app.on_event('startup')
async def startup() -> None:
    if not database.is_connected:
        await database.connect()
    await User.objects.get_or_create(email='test@test.com')


@app.on_event('shutdown')
async def shutdown() -> None:
    if database.is_connected:
        await database.disconnect()
