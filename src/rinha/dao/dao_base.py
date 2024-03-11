from rinha.db_connection import DatabaseConnection

class DAOBase:
    _db: DatabaseConnection

    def __init__(self, db: DatabaseConnection):
        self._db = db

    def begin(self):
        self._db.begin()
    
    def commit(self):
        self._db.commit()
    
    def rollback(self):
        self._db.rollback()