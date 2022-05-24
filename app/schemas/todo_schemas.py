from pydantic import BaseModel


class CreatedTask(BaseModel):
    title: str
    description: str
    user: str
    priority: str
    tag: str


