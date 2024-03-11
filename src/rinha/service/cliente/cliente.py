from rinha.dto.cliente.cliente import Cliente
from rinha.dao.cliente.cliente import ClienteDAO
from rinha.exception.not_found import NotFoundException

class ClienteService:
    def __init__(self, dao: ClienteDAO):
        self._dao = dao
    
    def lock_cliente(self, id: int):
        self._dao.lock_cliente(id)

    def get(self, id: int):
        result = self._dao.get_by_id(id)
        if len(result) == 0:
            raise NotFoundException("Cliente não encontrado")
        return Cliente(**result[0])
    
    def update_saldo(self, cliente: Cliente):
        self._dao.update_saldo(cliente)