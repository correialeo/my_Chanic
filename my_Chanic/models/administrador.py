from .user import User
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Administrador(User):
    def __init__(self, login: str, senha: str, nome: str, email: str, cargo: str, dt_admissao: datetime):
        super().__init__(login, senha)
        self.nome = nome
        self.email = email
        self.cargo = cargo
        self.dt_admissao = dt_admissao
        self.oficinas = {}
        self.clientes = {}

    def criar_conta_oficina(self, nome_oficina: str, endereco: str, senha_oficina: str) -> str:
        if nome_oficina in self.oficinas:
            return "Já existe uma Oficina com esse nome."
        self.oficinas[nome_oficina] = {"endereco": endereco, "senha": senha_oficina}
        return "Conta da oficina criada com sucesso!"

    def criar_conta_cliente(self, login_cliente: str, senha_cliente: str) -> str:
        if login_cliente in self.clientes:
            return "Já existe um cliente com esse login"
        self.clientes[login_cliente] = {"senha": senha_cliente}
        return "Cliente criado com sucesso!"

    def remover_conta_oficina(self, nome_oficina: str) -> str:
        if nome_oficina in self.oficinas:
            del self.oficinas[nome_oficina]
            return "Oficina removida com sucesso!"
        return "Oficina não encontrada."

    def remover_conta_cliente(self, login_cliente: str) -> str:
        if login_cliente in self.clientes:
            del self.clientes[login_cliente]
            return "Cliente removido com sucesso!"
        return "Cliente não encontrado."

    def gerar_relatorio_clientes(self) -> list:
        relatorio_clientes = []

        return relatorio_clientes

    def gerar_relatorio_oficina(self) -> list:
        relatorio_oficinas = []

        return relatorio_oficinas

    def notificar_clientes(self) -> None:
        pass

    def notificar_oficinas(self) -> None:
        pass

    def __str__(self) -> str:
        return f"Administrador: {self.nome}\nEmail: {self.email}\nCargo: {self.cargo}\nData de Admissão: {self.dt_admissao}"
