from pydantic import BaseModel, Extra


class Electronic(BaseModel):
    id: int
    brand: str
    category: str

    class Config:
        extra = Extra.allow
