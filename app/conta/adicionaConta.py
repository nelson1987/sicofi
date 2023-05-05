from domain.entities.conta import Conta

# Definimos o comando "AdicionarConta"
class AdicionaContaCommand:
    def __init__(self, nome, data_inicio, saldo_inicial):
        self.nome = nome
        self.data_inicio = data_inicio
        self.saldo_inicial = saldo_inicial

    def to_entity(self) -> Conta:
        return Conta(self.nome, self.data_inicio, self.saldo_inicial)

# Definimos o manipulador de comando "ManipuladorAdicionarConta"
class AdicionaContaHandler:
    def __init__(self, repositorio_contas):
        self.repositorio_contas = repositorio_contas

    def __call__(self, comando):
        conta = comando.to_entity()
        self.repositorio_contas.adicionar(conta)

class ListaContaHandler:
    def __init__(self, repositorio_contas):
        self.repositorio_contas = repositorio_contas

    def __call__(self, comando):
        #conta = comando.to_entity()
        self.repositorio_contas.listar()