from typing import OrderedDict

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from api.db.schemas import Blog, InMemoryDB

router = APIRouter()

db = InMemoryDB()
db.blogs = {
    1: Blog(
        id=1,
        title="The Hobbit",
        body="A blog by J.R.R. Tolkien about the Hobbit",
        is_published=False,
    ),
    2: Blog(
        id=2,
        title="The Lord of the Rings",
        body="A blog by J.R.R. Tolkien about the J.R.R. Tolkien about the Lord of the Rings",
        is_published=True,
    ),
    3: Blog(
        id=3,
        title="The Return of the King",
        body="A blog by J.R.R. Tolkien about the J.R.R. Tolkien about the Return of the King",
        is_published=True,
    ),
}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_blog(blog: Blog):
    db.add_blog(blog)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=blog.model_dump())


@router.get("/{blog_id}", response_model=Blog, status_code=status.HTTP_200_OK)
async def get_blog(blog_id: int):
    blog = db.blogs.get(blog_id)
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="blog not found"
        )
    return blog


@router.get("/", response_model=OrderedDict[int, Blog], status_code=status.HTTP_200_OK)
async def get_blogs() -> OrderedDict[int, Blog]:
    return db.get_blogs()


@router.put("/{blog_id}", response_model=Blog, status_code=status.HTTP_200_OK)
async def update_blog(blog_id: int, blog: Blog) -> Blog:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=db.update_blog(blog_id, blog).model_dump(),
    )


@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(blog_id: int) -> None:
    db.delete_blog(blog_id)
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)
