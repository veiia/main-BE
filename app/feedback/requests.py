from pydantic import BaseModel

from feedback.utils import FeedbackThemes


class CreateFeedbackRequest(BaseModel):
    theme: FeedbackThemes
    text: str
    user: str
