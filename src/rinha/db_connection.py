import sqlalchemy
from sqlparams import SQLParams
from sqlalchemy.engine.base import Connection
from rinha.settings import DATABASE_HOST, DATABASE_NAME, DATABASE_PASS, DATABASE_PORT, DATABASE_USER

class DatabaseConnection:
    _db: Connection

    def __enter__(self):
        database_conn_url = f"postgresql+pg8000://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

        pool = sqlalchemy.create_engine(database_conn_url, poolclass=sqlalchemy.pool.NullPool)

        self._db = pool.connect()
        self._transaction = None

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._db.close()
    
    def begin(self):
        if self._transaction is None:
            self._transaction = self._db.begin()

    def commit(self):
        if self._transaction is not None:
            self._transaction.commit()
            self._transaction = None

    def rollback(self):
        if self._transaction is not None:
            self._transaction.rollback()
            self._transaction = None

    def in_transaction(self):
        return self._transaction is not None

    def execute(self, sql: str, **kwargs) -> int:
        cur = None
        try:
            cur = self._execute(sql, **kwargs)

            return cur.rowcount
        finally:
            if cur is not None:
                cur.close()

    def execute_query(self, sql: str, **kwargs) -> list:
        cur = None
        try:
            cur = self._execute(sql, **kwargs)
            rs = cur.fetchall()

            return [dict(rec.items()) for rec in rs]
        finally:
            if cur is not None:
                cur.close()

    def _execute(self, sql: str, **kwargs):

        new_transaction = not self.in_transaction()

        try:
            if new_transaction:
                self.begin()

            if (kwargs is not None):
                pars = {key: kwargs[key] for key in kwargs}
                sql2, pars2 = SQLParams('named', 'format').format(sql, pars)
                return self._db.execute(sql2, pars2)
            else:
                return self._db.execute(sql)
        except:
            if new_transaction:
                self.rollback()
            raise

        finally:
            if new_transaction:
                self.commit()