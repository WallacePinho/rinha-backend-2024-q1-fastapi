from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    limite: int
    saldo: int