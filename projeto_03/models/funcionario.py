from models.enums.setor import Setor
from models.enums.sexo import Sexo
from models.endereco import Endereco


class Funcionario:
    def __init__(self, id: str, nome: str, cpf: str, rg: str, matricula: str, dataNascimento: str, salario: float, telefone: str, email: str, setor: Setor, genero: Sexo, endereco: Endereco) -> None:
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.matricula = matricula
        self.dataNascimento = dataNascimento
        self.salario = salario
        self.telefone = telefone
        self.email = email
        self.setor = setor
        self.sexo = genero
        self.endereco = endereco

    def __str__(self) -> str:
        return(
            "*== DADOS DO FUNCIONARIO ==*"
            f"\nID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nCPF: {self.cpf}"
            f"\nRG: {self.rg}"
            f"\nMatricula: {self.matricula}"
            f"\nData de nascimento: {self.dataNascimento}"
            f"\nSálario: {self.salario}"
            f"\nTelefone: {self.telefone}"
            f"\nE-mail: {self.email}"
            f"\nSetor: {self.setor.value}"
            f"\nSexo: {self.sexo.value}"
            f"\n\n-- ENDEREÇO --: {self.endereco}"
        )