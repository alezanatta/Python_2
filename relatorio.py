class Usuario:
    def __init__(self, nome: str, mbs: float, id: int) -> None:
        self.nome = nome
        self.mbs = mbs
        self.id = id
    
    def converte(self):
        convertido = self.mbs / 1048576
        return convertido
    
    #def total
    
    def porcentagem(self):
        Usuario.converte()
        ...


class Relatorio(Usuario):
    def __init__(self, nome: str, mbs: float, id: int) -> None:
        ...

relatorio = Relatorio("alexandre", 456123789)

print(relatorio.converte())
