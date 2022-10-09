from pydantic import BaseModel, Field

class UserModel(BaseModel):
    name: str = Field(...)