from pydantic import BaseModel


class Trol(BaseModel):
    name: str

tr = Trol(name = 'dfsdf')

print(tr)