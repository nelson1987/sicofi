from domain.entities.movimentacao import Movimentacao

class Conta:
    def __init__(self, nome, data_inicio, saldo_inicial):
        self.nome = nome
        self.data_inicio = data_inicio
        self.saldo = saldo_inicial
        self.movimentacoes = []
    
    def adiciona_movimentacao_debito(self, descricao, data, valor):
        movimentacao = Movimentacao(descricao, data, -valor)
        self.movimentacoes.append(movimentacao)
        self.saldo -= valor
    
    def adiciona_movimentacao_credito(self, descricao, data, valor):
        movimentacao = Movimentacao(descricao, data, valor)
        self.movimentacoes.append(movimentacao)
        self.saldo += valor
