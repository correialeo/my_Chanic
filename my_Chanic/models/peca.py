from dataclasses import dataclass

@dataclass
class Peca:
    _nome_peca: str
    _categoria_peca: str
    _valor_peca: float
    _qtd_pecas: float

    def __str__(self):
        return f"Nome da peça: {self._nome_peca}\nCategoria da peça: {self._categoria_peca}\nValor da peça: {self._valor_peca}\""