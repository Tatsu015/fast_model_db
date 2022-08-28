from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id:int
    name:str
