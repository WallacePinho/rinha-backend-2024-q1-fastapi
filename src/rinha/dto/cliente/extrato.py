from pydantic import BaseModel
from rinha.dto.cliente.transacao import Transacao
from rinha.dto.cliente.saldo import Saldo

class Extrato(BaseModel):
    saldo: Saldo
    ultimas_transacoes: list[Transacao]