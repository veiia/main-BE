import ormar as orm

from app.settings.db import BaseMeta
from profile.models import User


class Activity(orm.Model):
    class Meta(BaseMeta):
        tablename = 'activity'

    id: int = orm.Integer(primary_key=True)
    action: str = orm.String(max_length=256, nullable=False)
    out: str = orm.Text(nullable=False)
    origin: str = orm.String(max_length=256, nullable=False) # краткое описание источника происхождения лога
    user = orm.ForeignKey(User)
