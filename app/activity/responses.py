from pydantic import BaseModel


class AbstractActivityResponse(BaseModel):
    action: str
    out: str
    origin: str


class ActivityContainerResponse(AbstractActivityResponse):
    container_id: int


class ListActivityContainerResponse(BaseModel):
    activity: list[ActivityContainerResponse]


class ActivityUserResponse(AbstractActivityResponse):
    user_id: int


class ListActivityUserResponse(BaseModel):
    activity: list[ActivityUserResponse]
