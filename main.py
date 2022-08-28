from fastapi import FastAPI
from sqlmodel import Session, SQLModel, create_engine
from user import User

app = FastAPI()
engine = create_engine("sqlite:///db/user.db")
SQLModel.metadata.create_all(engine)

# with Session(engine) as session:


@app.get("/")
async def root():
    return {"message": "Hello World"}
