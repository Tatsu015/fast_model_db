from fastapi import FastAPI
from sqlmodel import Session, SQLModel, create_engine, select
from user import User

app = FastAPI()
engine = create_engine("sqlite:///db/user.db")

@app.get("/")
async def root():
    results = None
    with Session(engine) as session:
        statement = select(User)
        results = session.exec(statement)
        for u in results:
            print(f"--------------------------")
            print(f"ID   : {u.id}")
            print(f"NAME : {u.name}")
            print(f"type : {type(u)}")

    print(results)
    return results
