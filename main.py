from fastapi import FastAPI
from sqlmodel import Session, SQLModel, create_engine, select
from users import Users

app = FastAPI()
engine = create_engine("sqlite:///db/users.db")

@app.get("/")
async def root():
    results = None
    with Session(engine) as session:
        statement = select(Users)
        results = session.exec(statement)
        for u in results:
            print(f"--------------------------")
            print(f"ID   : {u.id}")
            print(f"NAME : {u.name}")
            print(f"type : {type(u)}")

    print(results)
    return results
