from pydantic import BaseModel
from rinha.enum.tipo_transacao import TipoTransacao
from datetime import datetime

class Transacao(BaseModel):
    valor: int
    tipo: TipoTransacao
    descricao: str
    realizada_em: datetime 