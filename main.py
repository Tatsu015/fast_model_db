from fastapi import FastAPI
from sqlmodel import Session, SQLModel, create_engine, select
from users import Users

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