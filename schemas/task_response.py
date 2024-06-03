from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: Optional[str] = None
    completed: bool = False
