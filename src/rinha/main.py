from rinha.settings import app


import rinha.controller.ping_controller
import rinha.controller.cliente.extrato_controller
import rinha.controller.cliente.transacao_controller


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)