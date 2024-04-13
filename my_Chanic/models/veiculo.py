from dataclasses import dataclass

@dataclass
class Veiculo:
    _fabricante_veiculo: str
    _placa: str
    _ano_modelo: int
    _dono: str

    def __str__(self):
        return f'Fabricante do veículo: {self._fabricante_veiculo}\nPlaca: {self._placa}\nAno Modelo: {self._ano_modelo}\nDono: {self._dono}'
