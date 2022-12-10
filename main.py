import os
from users import Users
from sqlmodel import Session, create_engine, select
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
url = f'mysql+pymysql://{os.getenv("MYSQL_USER")}:{os.getenv("MYSQL_PASSWORD")}@db:3306/{os.getenv("MYSQL_DB")}'
engine = create_engine(url, echo=True)

app.mount("/static", StaticFiles(directory="out"), name="static")

@app.get("/")
async def root():
    return "ok"


@app.get("/show", response_model=list[Users])
async def show():
    with Session(engine) as session:
        statement = select(Users)
        items = session.exec(statement).all()
        print(items)
        return items
    return '/show has error'


@app.post("/add")
async def add(users: list[Users]):
    with Session(engine) as session:
        for user in users:
            session.add(user)
        session.commit()
        return users
    return '/add has error'


@app.delete("/delete")
async def delete(ids: list[str]):
    print(ids)
    with Session(engine) as session:
        deleteds = []
        for id in ids:
            statement = select(Users).where(Users.id == id)
            items = session.exec(statement)
            user = items.one()
            session.delete(user)
            deleteds.append(user)
            session.commit()
        return deleteds
    return '/delete has error'


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
