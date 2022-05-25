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



@router.delete("/api/deleted_task", status_code=status.HTTP_200_OK)
async def deleted_task(payload: todo_schemas.DeletedTask):
    delete = await database.delete_task({"title":payload.title})
    return delete


@router.get("/api/get_all", status_code=status.HTTP_200_OK)
async def get_all():
     show = await database.get_show()
     return show


#@router.patch("/api/edit_task", status_code=status.HTTP_200_OK)
#async def edit_task():
#    edit = await database.edit_id()
#    return edit