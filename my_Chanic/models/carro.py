from .veiculo import Veiculo
from dataclasses import dataclass

@dataclass
class Carro(Veiculo):
    _modelo: str

    def __str__(self):
        return (f"{super().__str__()}\nModelo: {self._modelo}")