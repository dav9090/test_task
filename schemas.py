from pydantic import BaseModel
from typing import List

class ActivitySchema(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class BuildingSchema(BaseModel):
    id: int
    address: str
    latitude: float
    longitude: float
    class Config:
        orm_mode = True

class OrganizationSchema(BaseModel):
    id: int
    name: str
    phones: str
    building: BuildingSchema
    activities: List[ActivitySchema]
    class Config:
        orm_mode = True
