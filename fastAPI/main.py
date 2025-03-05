from fastapi import FastAPI
from pydantic import BaseModel

class RecipeInfo(BaseModel):
    title: str
    ingredients: list
    servings: int
    instructions: list