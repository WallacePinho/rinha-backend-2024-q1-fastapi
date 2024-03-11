from pydantic import BaseModel
from rinha.enum.tipo_transacao import TipoTransacao

class PostTransacaoResult(BaseModel):
    limite: int
    saldo: int