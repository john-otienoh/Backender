from pydantic import BaseModel
from enum import Enum
from typing import OrderedDict

class Blog(BaseModel):
    """Post Schema"""
    id: int
    title: str
    body: str
    is_published: bool = True

class InMemoryDB:
    def __init__(self) -> None:
        self.blogs: OrderedDict[int, Blog]

    def get_blogs(self) -> OrderedDict[int, Blog]:
        """Gets blogs from the database
        
        Returns:
            OrderedDict[int, Blog]: Ordered dictionary of blogs."""
        return self.blogs
    
    def create_blog(self, blog: Blog) -> Blog:
        """Adds book to database.

        Args:
            blog (Blog): Blog to create.

        Returns:
            Blog: Added blog.
        """
        self.blogs.update({blog.id: blog})
