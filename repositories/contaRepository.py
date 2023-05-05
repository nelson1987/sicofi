from baseDados import CONTAS_REPO


class ContaRepository:
    def adicionar(self, conta):
        CONTAS_REPO.append(conta)
        print(conta.saldo)
        return conta

    def listar(self):
        for x in CONTAS_REPO:
            print(x.nome)
