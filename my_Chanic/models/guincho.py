from dataclasses import dataclass


@dataclass
class Guincho:
    _localizacao_veiculo: str
    _localizacao_destino: str
    _status: str
    _valor: float
    _veiculo_transportado: str

    def __str__(self):
        return (f"Localizacao de Veiculo: {self._localizacao_veiculo}\nLocalizacao de Destino: {self._localizacao_destino}\nStatus: {self._status}\nValor: {self._valor}\nVeiculo Transportado: {self._veiculo_transportado}")