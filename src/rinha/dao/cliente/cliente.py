from rinha.db_connection import DatabaseConnection
from rinha.dto.cliente.cliente import Cliente
from rinha.dao.dao_base import DAOBase

class ClienteDAO(DAOBase):

    def __init__(self, db: DatabaseConnection):
        self._db = db
    
    def lock_cliente(self, id: int):
        sql = "select pg_advisory_xact_lock(:id);"

        return self._db.execute(sql, id=id)

    def get_by_id(self, id: int):
        sql = "select id, limite, saldo from rinha.cliente where id = :id;"

        return self._db.execute_query(sql, id=id)
    
    def update_saldo(self, cliente: Cliente):
        sql = "update rinha.cliente set saldo = :saldo where id = :id"

        self._db.execute(sql, **cliente.model_dump())

