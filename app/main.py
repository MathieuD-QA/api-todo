from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api_v1.endpoints import todo
api = FastAPI()
api.include_router(todo.router)


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://192.168.1.40:3000"
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@api.get("/")
async def root():
    return {"status": "OK"}
