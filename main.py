from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import crud

app = FastAPI()

class TaskCreate(BaseModel): # BaseModel is a Pydantic validation
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool

def row_to_dict(row): # Turns a database row into a dictionary
    return {
        "id": row[0],
        "title": row[1],
        "description": row[2],
        "completed": row[3],
        "created_at": row[4],
    }

@app.post("/tasks/")
def create_task(task: TaskCreate):
    row = crud.create_task(task.title, task.description)
    return row_to_dict(row)

@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    row = crud.get_task(task_id)
    if row is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return row_to_dict(row)

@app.get("/tasks/")
def read_tasks():
    return [row_to_dict(r) for r in crud.get_tasks()]

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):
    row = crud.update_task(task_id, task.title, task.description, task.completed)
    if row is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return row_to_dict(row)
