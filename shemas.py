from pydantic import BaseModel, ConfigDict
from typing import Optional

class TaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class Task(TaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)

class TaskId(BaseModel):
    ok: bool = True
    task_id: int