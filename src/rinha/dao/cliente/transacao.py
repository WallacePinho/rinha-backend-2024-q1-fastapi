from rinha.db_connection import DatabaseConnection
from rinha.dto.cliente.post_transacao import PostTransacao
from rinha.dao.dao_base import DAOBase

class TransacaoDAO(DAOBase):

    def __init__(self, db: DatabaseConnection):
        self._db = db
    
    def insert_transacao(self, cliente_id: int, transacao: PostTransacao):
        sql = "insert into rinha.transacao (cliente_id, valor, tipo, descricao, realizada_em) values (:cliente_id, :valor, :tipo, :descricao, now());"

        self._db.execute(sql, cliente_id=cliente_id, **transacao.model_dump())

    def list_by_cliente(self, cliente_id, limit: int):
        sql = "select valor, tipo, descricao, realizada_em from rinha.transacao where cliente_id = :cliente_id order by realizada_em desc limit :limit"

        return self._db.execute_query(sql, cliente_id=cliente_id, limit=limit)

