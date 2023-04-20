import ormar as orm

from app.settings.db import BaseMeta
from profile.models import User


class AbstractActivity(orm.Model):
    id: int = orm.Integer(primary_key=True)
    action: str = orm.String(max_length=256, nullable=False)
    out: str = orm.Text(nullable=False)
    origin: str = orm.String(
        max_length=256, nullable=False
    )  # краткое описание источника происхождения лога


class UserActivity(AbstractActivity):
    class Meta(BaseMeta):
        tablename = "user_activity"

    user = orm.ForeignKey(User)


class ContainerActivity(AbstractActivity):
    class Meta(BaseMeta):
        tablename = "container_activity"

    # container_id = orm.ForeignKey(Container)
