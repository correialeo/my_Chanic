from datetime import datetime
from .user import User

class Cliente(User):
    def __init__(self, login: str, senha: str, email: str, nome: str, idade: int, documento: str, carro: str):
        super().__init__(login, senha)
        self.email = email
        self.nome = nome
        self.idade = idade
        self.documento = documento
        self.carro = carro

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, value: str) -> None:
        self._nome = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        self._email = value

    @property
    def idade(self) -> int:
        return self._idade

    @idade.setter
    def idade(self, value: int) -> None:
        self._idade = value

    @property
    def documento(self) -> str:
        return self._documento

    @documento.setter
    def documento(self, value: str) -> None:
        self._documento = value

    @property
    def carro(self) -> str:
        return self._carro

    @carro.setter
    def carro(self, value: str) -> None:
        self._carro = value

    def iniciar_chat_ia(self) -> None:
        pass

    def solicitar_guincho(self) -> None:
        pass

    def pagar_servico(self) -> None:
        pass

    def servicoManutencao(self) -> None:
        pass

    def historico_de_servicos(self) -> list:
        historico_servicos = []
        return historico_servicos

