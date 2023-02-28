from pydantic import BaseModel


class Record(BaseModel):
    name: str
    value: str
