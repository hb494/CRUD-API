from datetime import datetime
from typing import Optional

# This is a model of the task table in the database

class Task:
    def __init__(
        self, 
        id: int, 
        title: str, 
        description: Optional[str], 
        completed: bool, 
        created_at: datetime = None
        ):

        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at