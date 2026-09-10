from database import get_db

def create_task(title:str, description: str | None = None):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (title, description) VALUES (%s, %s) "
        "RETURNING id, title, description, completed, created_at;", # so we know what id
        (title, description),
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return row

def get_task(task_id: int):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, title, description, completed, created_at FROM tasks WHERE id = %s;",
        (task_id,),
    )
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def get_tasks():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, title, description, completed, created_at FROM tasks ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def delete_task(task_id: int):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s RETURNING id;", (task_id,))
    deleted = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return deleted

def update_task(task_id: int, title: str, description: str, completed: bool):
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "UPDATE tasks SET title = %s, description = %s, completed = %s WHERE id = %s " 
        "RETURNING id, title, description, completed, created_at;", 
        (title, description, completed, task_id)
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return row