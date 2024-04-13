from dataclasses import dataclass
from datetime import datetime
from typing import List
from my_Chanic.models import endereco

@dataclass
class Oficina:
    _nome: str
    _endereco: endereco
    _email: str
    _horario_funcionamento: datetime
    _servicos_oferecidos: List[str]
    _historico_servicos: List[str]
    _avaliacao: float

    def __str__(self):
        horario_formatado = self._horario_funcionamento.strftime("%H:%M")
        return (f'Oficina {self._nome}\nEndereço: {self._endereco}\nHorário de Funcionamento: {horario_formatado}\n'
                f'Serviços Oferecidos: {self._servicos_oferecidos}\nAvaliação: {self._avaliacao}')