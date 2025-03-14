from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()
users: List[str] = []

@app.post("/add-user/")
async def add_user(name: str):
    if name in users:
        raise HTTPException(status_code=400, detail="Ім'я вже існує")
    users.append(name)
    return {"message": "Ім'я додано", "name": name}

@app.get("/get-users/")
async def get_users():
    return {"users": users}

@app.delete("/delete-user/")
async def delete_user(name: str):
    if name not in users:
        raise HTTPException(status_code=404, detail="Ім'я не знайдено")
    users.remove(name)
    return {"message": "Ім'я видалено", "name": name}
