from fastapi import FastAPI
from sqlmodel import Session, SQLModel, create_engine, select
from users import Users
from typing import Optional

app = FastAPI()
engine = create_engine("sqlite:///db/users.db")


@app.get("/")
async def root():
    return "ok"


@app.get("/show", response_model=list[Users])
async def show():
    with Session(engine) as session:
        statement = select(Users)
        items = session.exec(statement).all()
        return items
    return []
