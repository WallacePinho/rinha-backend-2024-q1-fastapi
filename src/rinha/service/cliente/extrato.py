from rinha.dto.cliente.extrato import Transacao
from rinha.service.cliente.cliente import ClienteService
from rinha.service.cliente.transacao import TransacaoService
from datetime import datetime

class ExtratoService:
    def __init__(self, cliente_service: ClienteService, transacao_service: TransacaoService):
        self._cliente_service = cliente_service
        self._transacao_service = transacao_service
    
    def monta_extrato(self, cliente_id: int):
        cliente = self._cliente_service.get(cliente_id)
        transacoes = self._transacao_service.list(cliente_id)

        extrato = {"saldo": {
                        "total": cliente.saldo,
                        "data_extrato": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "limite": cliente.limite
                    },
                   "ultimas_transacoes": transacoes}
        
        return extrato
