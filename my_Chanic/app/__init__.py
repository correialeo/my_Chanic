from my_Chanic.models.administrador import Administrador
from my_Chanic.models.carro import Carro
from my_Chanic.models.veiculo import Veiculo
from my_Chanic.models.endereco import Endereco


# adm1 = Administrador("Admin1", "123456", "Leandro", "abc123@mychanic.com.br", "CEO", "08/02/2024")
# nome = adm1.get_nome()
# print(nome)

# corvette = Carro("Carro", "ABC67DJ", 2023, "Pedro", "Corvette")
# placa = corvette.get_placa()
# print(placa)

myChanic = Endereco("Avenida Paulista", "São Paulo", "SP", "1106")
print(myChanic._cidade)
myChanic._cidade = "Rio de Janeiro"
print(myChanic._cidade)