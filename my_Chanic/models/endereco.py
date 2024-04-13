from dataclasses import dataclass

@dataclass
class Endereco:
    _logradouro: str
    _cidade: str
    _estado: str
    _numero: str

    def __str__(self):
        return f'Logradouro: {self._logradouro}\nCidade: {self._cidade}\nEstado: {self._estado}\nNumero: {self._numero}'