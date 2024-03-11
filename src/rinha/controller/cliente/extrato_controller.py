from fastapi import HTTPException
from rinha.settings import app
from rinha.db_connection import DatabaseConnection
from rinha.exception.not_found import NotFoundException
from rinha.dao.cliente.cliente import ClienteDAO
from rinha.dao.cliente.transacao import TransacaoDAO
from rinha.service.cliente.cliente import ClienteService
from rinha.service.cliente.transacao import TransacaoService
from rinha.service.cliente.extrato import ExtratoService

@app.get("/clientes/{cliente_id}/extrato")
def get_extrato(cliente_id: int):
    with DatabaseConnection() as connection:
        try:
            # DAOs
            cliente_dao = ClienteDAO(connection)
            transacao_dao = TransacaoDAO(connection)
            # Services
            cliente_service = ClienteService(cliente_dao)
            transacao_service = TransacaoService(transacao_dao, cliente_service)
            service = ExtratoService(cliente_service, transacao_service)

            return service.monta_extrato(cliente_id)
        except NotFoundException as e:
            raise HTTPException(status_code=404, detail=str(e))