from pydantic import BaseModel
from typing import Optional

class DroneBase(BaseModel):
    name: str
    model: str

class DroneCreate(DroneBase):
    price: Optional[float] = None
    description: Optional[str] = None

class DroneOut(DroneBase):
    id: int
    image: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True
