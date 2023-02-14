class Funcionario:
    def __init__(self, nome, cargo, salario) -> None:
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def __str__(self) -> str:
        return(f"{self.nome}, {self.cargo}, {self.salario}")

class Cliente:
    def __init__(self, nome, cep, telefone) -> None:
        self.nome = nome
        self.cep = cep
        self.telefone = telefone

    def __str__(self) -> str:
        return(f"{self.nome}, {self.cep}, {self.telefone}")

class Produto:
    def __init__(self, nome, preco, validade) -> None:
        self.nome = nome
        self.preco = preco
        self.validade = validade

    def __str__(self) -> str:
        return(f"{self.nome}, {self.preco}, {self.validade}")