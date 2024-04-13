from dataclasses import dataclass

@dataclass
class Servico:
    codigo_de_servico: str
    tipo_servico: str
    valor_servico: float

    def __str__(self):
        return f"Código de serviço: {self.codigo_de_servico}\nTipo do serviço: {self.tipo_servico}\n Valor: {self.valor_servico}"