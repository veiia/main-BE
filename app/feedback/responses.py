from feedback.utils import FeedbackThemes


class FeedbackResponse:
    theme: FeedbackThemes
    text: str
    user: str


class ListFeedbacksResponse:
    feedbacks: list[FeedbackResponse]
