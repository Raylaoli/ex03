from models.enums.setor import Setor
from models.enums.sexo import Sexo


class Funcionario:
    def __init__(self, id: str, nome: str, idade: int, salario: float, setor: Setor, genero: Sexo) -> None:
        self.id = id
        self.nome = nome
        self.idade =  idade
        self.salario = salario
        self.setor = setor
        self.sexo = genero

    def __str__(self) -> str:
        return(
            "*== DADOS DO FUNCIONARIO ==*"
            f"\nID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nIdade: {self.idade}"
            f"\nSalario: {self.salario}"
            f"\nSetor: {self.setor.value}"
            f"\nSexo: {self.sexo.value}"
        )