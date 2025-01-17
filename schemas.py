from pydantic import BaseModel

class RecipeBase(BaseModel):
    title: str
    preparation_time: int
    ingredients: str
    description: str

class RecipeCreate(RecipeBase):
    pass

class RecipeResponse(RecipeBase):
    id: int
    views: int

    class Config:
        from_attributes = True