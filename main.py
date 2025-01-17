from fastapi import FastAPI, HTTPException, Depends
from typing import List
from database import init_db, get_db
from models import Recipe
from schemas import RecipeCreate, RecipeResponse
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI(title="Culinary Book API", description="API для управления кулинарной книгой", version="1.0.0")

@app.get("/recipes", response_model=List[RecipeResponse])
async def get_recipes(db: AsyncSession = Depends(get_db)):
    """Получить список всех рецептов, отсортированных по популярности и времени приготовления."""
    result = await db.execute(
        """SELECT * FROM recipes ORDER BY views DESC, preparation_time ASC"""
    )
    recipes = result.scalars().all()
    return recipes

@app.get("/recipes/{recipe_id}", response_model=RecipeResponse)
async def get_recipe(recipe_id: int, db: AsyncSession = Depends(get_db)):
    """Получить детальную информацию о рецепте по его ID."""
    result = await db.execute(
        """SELECT * FROM recipes WHERE id = :id""",
        {"id": recipe_id}
    )
    recipe = result.scalar()
    if not recipe:
        raise HTTPException(status_code=404, detail="Рецепт не найден")
    recipe.views += 1
    db.add(recipe)
    await db.commit()
    await db.refresh(recipe)
    return recipe

@app.post("/recipes", response_model=RecipeResponse)
async def create_recipe(recipe: RecipeCreate, db: AsyncSession = Depends(get_db)):
    """Создать новый рецепт."""
    new_recipe = Recipe(
        title=recipe.title,
        preparation_time=recipe.preparation_time,
        ingredients=recipe.ingredients,
        description=recipe.description
    )
    db.add(new_recipe)
    await db.commit()
    await db.refresh(new_recipe)
    return new_recipe


if '__main__' == __name__:
    import asyncio
    asyncio.run(init_db())