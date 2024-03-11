from fastapi import HTTPException
from rinha.settings import app
from rinha.db_connection import DatabaseConnection
from rinha.exception.not_found import NotFoundException
from rinha.exception.sem_limite import SemLimiteException
from rinha.dao.cliente.cliente import ClienteDAO
from rinha.dao.cliente.transacao import TransacaoDAO
from rinha.service.cliente.cliente import ClienteService
from rinha.service.cliente.transacao import TransacaoService
from rinha.dto.cliente.post_transacao import PostTransacao

@app.post("/clientes/{cliente_id}/transacoes")
def post_transacao(cliente_id: int, transacao: PostTransacao):
    with DatabaseConnection() as connection:
        try:
            # DAOs
            cliente_dao = ClienteDAO(connection)
            transacao_dao = TransacaoDAO(connection)
            # Services
            cliente_service = ClienteService(cliente_dao)
            service = TransacaoService(transacao_dao, cliente_service)

            return service.create(cliente_id, transacao)
        except NotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))
        except SemLimiteException as e:
            raise HTTPException(status_code=422, detail=str(e))