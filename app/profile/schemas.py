from pydantic import BaseModel


class UserSchema(BaseModel):
    firstname: str

    class Config:
        orm_mode = True
