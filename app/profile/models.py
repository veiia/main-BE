from ormar import Boolean, Integer, Model, String

from app.settings.db import BaseMeta


class User(Model):
    class Meta(BaseMeta):
        tablename = 'users'

    id: int = Integer(primary_key=True)
    email: str = String(max_length=128, unique=True, nullable=False)
    active: bool = Boolean(default=True, nullable=False)
    firstname: str = String(max_length=128, unique=True, nullable=False)
    lastname: str = String(max_length=128, unique=True, nullable=False)
