from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from sql_examples.database import SessionLocal, User
from pydantic import BaseModel, Emailstr, field_validator
from nosql_examples.database import user_collection
from bson import ObjectId

app = FastAPI()

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
class Tweet(BaseModel):
    content: str
    hashtags: list[str]

class UserData(BaseModel):
    name: str
    email: Emailstr
    age: int
    tweets: list[Tweet] | None=None

    @field_validator("age")
    def validate_age(cls, value):
        if value < 18 or value > 100:
            raise ValueError(
                "Age must be between 18 and 100"
            )
        return value
    
@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}

@app.get("/users", status_code=status.HTTP_200_OK)
async def get_users(db: Session=Depends(get_db)):
    users = db.query(User).all()
    return users

# Creating a new User
@app.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserData,
    db: Session=Depends(get_db)
):
    new_user = User(
        name=user.name,
        email=user.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Getting Specific user
@app.get("/user/{user_id}", status_code=status.HTTP_200_OK)
async def get_user(
    user_id: int,
    db: Session=Depends(get_db)
):
    user = (
        db.query(User).filter(
            User.id == user_id
        ).first()
    )
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User Not Found!!!"
        )
    return user

# Updating a User
@app.patch("/user/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(
    user_id: int,
    user: UserData,
    db: Session=Depends(get_db)
):
    db_user = (
        db.query(User).filter(
            User.id == user_id
        ).first()
    )
    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User Not Found!!!"
        )
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return  db_user

# Deleting a user
@app.delete("/user{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    user: UserData,
    db: Session=Depends(get_db)
):
    db_user = (
        db.query(User).filter(
            User.id == user_id
        ).first()
    )
    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User Not Found!!!"
        )
    db.delete(db_user)
    db.commit()
    return {
        "message": "User deleted"
    }


"""
NO RELATIONAL DATABASES
"""
class UserResponse(User):
    id: str

# Getting all Users
@app.get("/musers")
async def read_users() -> list[User]:
    return [user for user in user_collection.find()]

# Creating a user
@app.post("/muser")
async def create_muser(user: User):
    result = user_collection.insert_one(
        user.model_dump(exclude_none=True)
    )
    user_responses = UserResponse(
        id=str(result.inserted_id),
        *user.model_dump()
    )

    return user_responses

# Getting a user
@app.get("/muser/{user_id}")
async def get_muser(user_id: str) -> UserResponse:
    db_user = user_collection.find_one(
        {
            "_id": ObjectId(user_id)
            if ObjectId.is_valid(user_id)
            else None
        }
    )
    if db_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    db_user["id"] = str(db_user["_id"])
    
    return db_user