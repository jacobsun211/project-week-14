from pydantic import BaseModel



class Data(BaseModel):
    id: int
    name: str
    email: str