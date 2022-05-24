from fastapi import APIRouter, status
from app.db import database
from app.schemas import todo_schemas

router = APIRouter()


@router.post("/api/created_task", status_code=status.HTTP_201_CREATED)
async def created_task(payload: todo_schemas.CreatedTask):
    create = await database.add_task(
        {"title": payload.title, "description": payload.description, "user": payload.user, "priority": payload.priority,
         "tag": payload.tag})
    return create

