from dataclasses import dataclass
from typing import List
from my_Chanic.models import peca

@dataclass
class Orcamento:
    _cliente: str
    _pecas_necessarias: List[peca]
    _mao_de_obra: float
    _status: str
    _valor_total: float

    def calcular_total_pecas(self):
        total_pecas = 0
        if self._pecas_necessarias is not None:
            for peca in self._pecas_necessarias:
                total_pecas += peca._valor_peca * peca._qtd_pecas
        return total_pecas

    def calcular_total(self):
        total_pecas = self.calcular_total_pecas()
        total = total_pecas + self._mao_de_obra
        return total

    def enviar_email_cliente(self):
        pass

    def __str__(self):
        return f'Orcamento: {self.calcular_total()}'