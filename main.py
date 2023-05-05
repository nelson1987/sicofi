
from app.conta.adicionaConta import AdicionaContaCommand, AdicionaContaHandler, ListaContaHandler
#from app.conta.adicionaMovimento import AdicionaMovimentoCommand, AdicionaMovimentoHandler
from domain.entities.cliente import Cliente
from domain.entities.conta import Conta
#from repositories.movimentoRepository import MovimentoRepository
from repositories.contaRepository import ContaRepository

# for x in CLIENTES_REPO:
#     print(x.nome)


cliente1 = Cliente("João")
conta1 = Conta("Conta Corrente", "01/01/2022", 1000.0)
cliente1.adiciona_conta(conta1)
#cliente1.adiciona_conta(conta2)
conta1.adiciona_movimentacao_credito("Salário", "01/02/2022", 3000.0)


#Adicionar Conta
repositorio_contas = ContaRepository()
manipulador = AdicionaContaHandler(repositorio_contas)
comando = AdicionaContaCommand("Minha Conta", "2023-05-05", 1000)
manipulador(comando)

#Adicionar Conta
repositorio_contas = ContaRepository()
manipulador = ListaContaHandler(repositorio_contas)
comando = AdicionaContaCommand("Minha Conta", "2023-05-05", 1000)
manipulador(comando)

##Adicionar Mopvimentacao
#repositorio_movimento = MovimentoRepository()
#manipulador = AdicionaMovimentoHandler(repositorio_movimento)
#comando = AdicionaMovimentoCommand("Conta Corrente", "Salário", "01/02/2022", 3000.0)
#manipulador(comando)
