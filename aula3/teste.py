class Gabriel:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def __str__(self) -> str:
        return(f"{self.nome}, {self.idade}")


gabriel = Gabriel("Gabriel vaida", 28)

print(gabriel)