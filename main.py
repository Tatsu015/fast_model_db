from fastapi import FastAPI
from sqlmodel import Session, SQLModel, create_engine
from user import User


app = FastAPI()

hero_1 = User(name="user1", id=1)
hero_2 = User(name="user2", id=2)
hero_3 = User(name="user3", id=3)


engine = create_engine("sqlite:///user.db")


SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()


@app.get("/")
async def root():
    return {"message": "Hello World"}