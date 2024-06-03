from fastapi import APIRouter, status, HTTPException
from schemas import task_request, task_response
from typing import List
from uuid import UUID, uuid4

router = APIRouter()
tasks_tags_metadata = {
    "name": "tasks",
    "description": "**Tasks** operations.",
}

tasks = []


@router.post(
    "",
    response_model=task_response.TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(_task_request: task_request.TaskRequest):

    _task_response = task_response.TaskResponse(
        id=uuid4(),
        title=_task_request.title,
        description=_task_request.description,
        completed=_task_request.completed,
    )

    tasks.append(_task_response)
    return _task_response


@router.get("/{task_id}", response_model=task_response.TaskResponse)
def read_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task

    raise HTTPException(status_code=404, detail="task not found.")


@router.get("", response_model=List[task_response.TaskResponse])
def read_tasks():
    return tasks


@router.put("/{task_id}", response_model=task_response.TaskResponse)
def update_task(task_id: UUID, task_update: task_request.TaskRequest):
    for index, _task in enumerate(tasks):
        if _task.id == task_id:
            updated_task = _task.model_copy(
                update=task_update.model_dump(exclude_unset=True)
            )
            updated_task.id = _task.id  # id cannot be updated
            tasks[index] = updated_task
            return updated_task

    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: UUID):
    for index, _task in enumerate(tasks):
        if _task.id == task_id:
            tasks.pop(index)
            return {"detail": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found!")
