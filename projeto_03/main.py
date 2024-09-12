import os

from models.endereco import Endereco
from models.enums.estado import Estado
from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.funcionario import Funcionario

os.system("cls || clear")

funcionario = Funcionario("2514", "Joana", "123.456.789-00", "12.345.678-99", "12345", "dd/mm/aaaa", 5000.00, "7199999-9999", "joana@gmail.com", Setor.JURIDICO, Sexo.FEMININO, 
                          Endereco("Rua A", "55", "proximo a lagoa", "12.300-000", "Xique-xique", Estado.BAHIA))

print(funcionario)