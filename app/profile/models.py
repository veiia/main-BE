import ormar as orm

from app.settings.db import BaseMeta


class User(orm.Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = orm.Integer(primary_key=True)
    email: str = orm.String(max_length=128, unique=True, nullable=False)
    is_active: bool = orm.Boolean(default=True, nullable=False)
    firstname: str = orm.String(max_length=128, unique=False, nullable=False)
    lastname: str = orm.String(max_length=128, unique=False)
    password: str = orm.String(max_length=128)
    is_light_theme: bool = orm.Boolean(default=True, nullable=False)
