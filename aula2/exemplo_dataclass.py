from datetime import date
from decimal import Decimal
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    cpf: str
    cep: str
    numero: int
    dt_nasc: date
    telefone: str


@dataclass
class Funcionario(Pessoa):
    salario: Decimal
    cargo: str


jonas_funcionario = Funcionario("Jonas" "444.555.666-89", "098877-123", 102, "21/12/1998",
                                "287321-2091", 3000, "Gerente", "Aaa")

print(jonas_funcionario.cargo)
