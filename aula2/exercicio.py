from datetime import date
from decimal import Decimal


class Pessoa:
    def __init__(self, nome: str, cpf: str, cep: str,
                 numero: int, dt_nasc: date, telefone: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.dt_nasc = dt_nasc
        self.cep = cep
        self.numero = numero
        self.telefone = telefone

    def verificar_cpf(self):
        pass


class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: str, cep: str,
                 numero: int, dt_nasc: date, telefone: str,
                 renda: Decimal):
        super().__init__(nome, cpf, cep, numero, dt_nasc, telefone)
        self.renda = renda



class Funcionario(Pessoa):
    def __init__(self, nome: str, cpf: str, cep: str,
                 numero: int, dt_nasc: date, telefone: str,
                 salario: Decimal, cargo: str) -> None:
        super().__init__(nome, cpf, cep, numero, dt_nasc, telefone)
        self.salario = salario
        self.cargo = cargo

    def marcar_ponto(self):
        pass

    def verificar_credito(self):
        pass


gabriel_cliente = Cliente("Gabriel" "111.222.333-89", "123456-123", 2039, "10/10/2001", "99293-2001", 1000)

jonas_funcionario = Funcionario("Jonas" "444.555.666-89", "098877-123", 102, "21/12/1998",
                                "287321-2091", 3000, "Gerente")
