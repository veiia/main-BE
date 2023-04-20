from fastapi import APIRouter, HTTPException

from app.settings.tags import Tags
from feedback.models import Feedback
from feedback.requests import CreateFeedbackRequest
from feedback.responses import FeedbackResponse, ListFeedbacksResponse
from feedback.utils import FeedbackThemes

router = APIRouter(
    prefix=f"/{Tags.FEEDBACK}",
    tags=[Tags.FEEDBACK],
    # dependencies=[Depends(get_token_header)],
    responses={
        404: {"description": "Not found"},
        403: {"description": "Permission Denied"},
    },
)


@router.get("/{feedback_id}", response_model=FeedbackResponse)
async def get_feedback(feedback_id: str) -> Feedback:
    feedback = await Feedback.objects.get_or_none(id=feedback_id)
    if not feedback:
        raise HTTPException(status_code=404, detail="Not found")
    return feedback


@router.post("/", response_model=FeedbackResponse)
async def create_feedback(feedback: CreateFeedbackRequest) -> Feedback:
    feedback = await Feedback.objects.update_or_create(feedback)
    if not feedback:
        raise HTTPException(status_code=400, detail="Bad Request")
    return feedback


@router.get("/", response_model=ListFeedbacksResponse)
async def get_list_of_feedbacks(user_id: str) -> None:
    feedbacks = await Feedback.objects.filter(user=user_id).all()
    return feedbacks


@router.get("/themes", response_model=ListFeedbacksResponse)
async def get_themes() -> dict[str, str]:
    return FeedbackThemes.to_dict()
