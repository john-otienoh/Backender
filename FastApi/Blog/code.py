from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    """Post Schema"""

    id: int
    title: str
    body: str
    is_published: bool = True


@app.get("/")
async def root():
    """Root API"""
    return {"message": "Hello World"}


@app.get("/posts")
async def posts():
    return {"posts": "These are my posts"}


@app.post("/create")
async def create_posts(post: Post):
    """Create New Post"""
    print(post)
    return {"message": "Post created successfully"}
