from pydantic import BaseModel, Field
from typing import List

class SubjectCreate(BaseModel):
    name: str
    classes_per_week: int = Field(gt=0)
    days: List[str]

class SubjectResponse(BaseModel):
    id: str
    name: str
    classes_per_week: int
    days: List[str]