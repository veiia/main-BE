import ormar as orm

from app.settings.db import BaseMeta
from feedback.utils import FeedbackThemes
from profile.models import User


class Feedback(orm.Model):
    class Meta(BaseMeta):
        tablename = "feedback"

    id: int = orm.Integer(primary_key=True)
    theme: str = orm.String(enum_class=FeedbackThemes, max_length=128)
    text: str = orm.Text(unique=False, nullable=False)
    user = orm.ForeignKey(User)
