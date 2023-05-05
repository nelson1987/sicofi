from domain.entities.conta import Conta
from domain.entities.movimentacao import Movimentacao

# Definimos o comando "AdicionarConta"
class AdicionaMovimentoCommand:
    def __init__(self, contaId, descricao, data, valor):
        self.contaId = contaId
        self.descricao = descricao
        self.data = data
        self.valor = valor

    def to_entity(self) -> Movimentacao:
        return Movimentacao(self.descricao, self.data, self.valor)

# Definimos o manipulador de comando "ManipuladorAdicionarConta"
class AdicionaMovimentoHandler:
    def __init__(self, repositorio_movimentos):
        self.repositorio_movimentos = repositorio_movimentos

    def __call__(self, comando):
        movimento = comando.to_entity()
        self.repositorio_movimentos.adicionar(comando.contaId,movimento)