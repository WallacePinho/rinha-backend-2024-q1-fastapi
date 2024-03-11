from rinha.dto.cliente.transacao import Transacao
from rinha.dto.cliente.post_transacao import PostTransacao
from rinha.dto.cliente.post_transacao_result import PostTransacaoResult
from rinha.dao.cliente.transacao import TransacaoDAO
from rinha.service.cliente.cliente import ClienteService
from rinha.enum.tipo_transacao import TipoTransacao
from rinha.exception.sem_limite import SemLimiteException

class TransacaoService:
    def __init__(self, dao: TransacaoDAO, cliente_service: ClienteService):
        self._dao = dao
        self._cliente_service = cliente_service
    
    def create(self, cliente_id: int, transacao: PostTransacao):
        try:
            self._dao.begin()

            self._cliente_service.lock_cliente(cliente_id)
            cliente = self._cliente_service.get(cliente_id)

            # realiza transacao
            if transacao.tipo is TipoTransacao.d:
                cliente.saldo -=  transacao.valor
                if cliente.saldo < 0 and (cliente.saldo*-1) > cliente.limite:
                    raise SemLimiteException("Cliente não possui limite disponível")
            if transacao.tipo is TipoTransacao.c:
                cliente.saldo += transacao.valor
            self._dao.insert_transacao(cliente_id, transacao)
            self._cliente_service.update_saldo(cliente)

            self._dao.commit()

            return PostTransacaoResult(**cliente.model_dump())
        except:
            self._dao.rollback()
            raise
    
    def list(self, cliente_id: int):
        return [Transacao(**transacao) for transacao in self._dao.list_by_cliente(cliente_id, 10)]