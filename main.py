
from app.conta.adicionaConta import AdicionaContaCommand, AdicionaContaHandler
from domain.entities.cliente import Cliente
from domain.entities.conta import Conta
from repositories.contaRepository import ContaRepository

cliente1 = Cliente("João")
conta1 = Conta("Conta Corrente", "01/01/2022", 1000.0)
conta2 = Conta("Conta Poupança", "01/01/2022", 500.0)
cliente1.adiciona_conta(conta1)
cliente1.adiciona_conta(conta2)

print(cliente1.saldo_total()) # Output: 1500.0

conta1.adiciona_movimentacao_credito("Salário", "01/02/2022", 3000.0)
conta1.adiciona_movimentacao_debito("Aluguel", "05/02/2022", 1000.0)

print(cliente1.saldo_total()) # Output: 3500.0


repositorio_contas = ContaRepository()
# Para usar o manipulador de comando, podemos injetá-lo em um controlador ou serviço
manipulador = AdicionaContaHandler(repositorio_contas)

# Então, quando o usuário solicitar adicionar uma nova conta, podemos criar um comando e enviá-lo para o manipulador
comando = AdicionaContaCommand("Minha Conta", "2023-05-05", 1000)
manipulador(comando)
