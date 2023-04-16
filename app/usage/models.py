import ormar as orm

from app.settings.db import BaseMeta
from profile.models import User


class Usage(orm.Model):
    class Meta(BaseMeta):
        tablename = 'usage'

    id: int = orm.Integer(primary_key=True)
    user = orm.ForeignKey(User)
