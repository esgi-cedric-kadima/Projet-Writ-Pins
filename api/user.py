from typing import List
from fastapi import APIRouter
from model.User import User
from repository.UserRepository import UserRepository

router = APIRouter(prefix="/users", )


@router.get("/", response_model=List[User])
async def read_users():
    users = UserRepository().get_all_users()
    return [{"id": i[0], "email": i[1], "password": i[2], "username": i[3], "bio": i[4], "image": i[5]} for i in users]


# Register
@router.post("/")
async def create_user(user: User):
    user_dict = user.dict()
    user_id = UserRepository().create_user(user_dict)
    return {**user_dict, "id": user_id}


# Login
@router.post("/login")
async def login_user(user: User):
    user_dict = user.dict()
    user = UserRepository().login(user_dict['email'], user_dict['password'])
    return {"id": user[0], "email": user[1], "password": user[2], "username": user[3], "bio": user[4], "image": user[5]}


# Get user
@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int):
    user = UserRepository().get_user(user_id)
    return {"id": user[0], "email": user[1], "password": user[2], "username": user[3], "bio": user[4], "image": user[5]}


# Update User
@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user: User):
    user_dict = user.dict()
    update_data = {
        "email": user_dict["email"],
        "password": user_dict["password"],
        "username": user_dict["username"],
        "bio": user_dict["bio"],
        "image": user_dict["image"],
        "id": user_id,
    }
    UserRepository().update_user(user_id, update_data)
    return {**update_data}
