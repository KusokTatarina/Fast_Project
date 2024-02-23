
from typing import Annotated
from fastapi import APIRouter, Depends
from repository import TaskRepository

from shemas import Task, TaskAdd, TaskId

router = APIRouter(
    prefix='/task', tags=['Таски']
)


@router.post('')
async def add_task(task: Annotated[TaskAdd, Depends()]) -> TaskId:
    task_id = await TaskRepository.add_one(task)
    return {'ok':True, 'task_id': task_id}


@router.get('')
async def get_task() -> list[Task]:
    task = await TaskRepository.find_all()
    return task
