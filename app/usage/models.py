import ormar as orm

from app.settings.db import BaseMeta
from profile.models import User


class Usage(orm.Model):
    class Meta(BaseMeta):
        tablename = "usage"

    id: int = orm.Integer(primary_key=True)
    # TODO: добавить значения какие-нибудь
    user = orm.ForeignKey(User)
