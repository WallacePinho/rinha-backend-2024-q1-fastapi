from pydantic import BaseModel
from datetime import datetime

class Saldo(BaseModel):
    total: int
    data_extrato: datetime
    limite: int