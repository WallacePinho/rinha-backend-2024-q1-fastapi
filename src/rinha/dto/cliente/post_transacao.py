from pydantic import BaseModel, Field
from rinha.enum.tipo_transacao import TipoTransacao

class PostTransacao(BaseModel):
    valor: int
    tipo: TipoTransacao
    descricao: str = Field(min_length=1, max_length=10)