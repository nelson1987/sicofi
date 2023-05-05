class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []
    
    def adiciona_conta(self, conta):
        self.contas.append(conta)
    
    def saldo_total(self):
        saldo_total = 0
        for conta in self.contas:
            saldo_total += conta.saldo
        return saldo_total