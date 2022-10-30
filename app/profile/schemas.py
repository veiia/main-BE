from pydantic import BaseModel


class UserUpdate(BaseModel):
    email: str | None
    firstname: str | None
    lastname: str | None
    password: str | None


class UserLogin(BaseModel):
    email: str
    password: str
    firstname: str | None
    lastname: str | None


class UserOut(BaseModel):
    email: str | None
    firstname: str | None
    lastname: str | None
    is_light_theme: bool | None

    class Config:
        orm_mode = True


class AppearanceSchema(BaseModel):
    is_light_theme: bool
