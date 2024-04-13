class User:
    def __init__(self, login, senha):
        self._login = login
        self._senha = senha

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, novo_login):
        self._login = novo_login

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha

    def validar_senha(self, senha):
        pass

    def autenticar(self):
        pass
