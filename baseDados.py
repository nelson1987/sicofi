from domain.entities.cliente import Cliente
from domain.entities.conta import Conta
from domain.entities.movimentacao import Movimentacao

CLIENTES_REPO  = [
    Cliente("João")
    ]

CONTAS_REPO  = [
    Conta("Conta Poupança", "01/01/2022", 500.0)
    ]

MOVIMENTOS_REPO  = [
    Movimentacao("Aluguel", "05/02/2022", 1000.0)
    ]