# Field permite añadir otras validaciones sobre los datos especificos.
from typing import Optional
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: Optional[int] = None
    name: str = Field(default="New Product", min_length=15)
    price: float = Field(default=0, ge=0, le=1000)
    stock: int = Field(gt=0)
