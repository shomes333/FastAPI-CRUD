from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED
from schema.user_schema import UserSchema
from config.db import conn
from model.users import users
from werkzeug.security import generate_password_hash, check_password_hash

user = APIRouter()


@user.get("/")
def root():
    return {"message": "Hola, soy FastAPI con un router"}

@user.post("/api/user", status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    new_user = data_user.dict()
    new_user["user_passw"] = generate_password_hash(data_user.user_passw, "pbkdf2:sha256:30", 30)
    
    conn.execute(users.insert().values(new_user))

    return Response(status_code=HTTP_201_CREATED)

@user.put("/api/user")
def update_user():
    pass