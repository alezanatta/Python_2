from typing import Union

class Veiculo:
    def __init__(self,
                marca: str,
                modelo: str,
                ano: Union[int, None] = None) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def girar_chave(self):
        if self.status == "desligado":
            self.status = "ligado"
        else:
            self.status = "desligado"

class Carro(Veiculo):
    def __init__(self,
                    marca: str,
                    modelo: str,
                    ano: Union[int, None] = None,
                    status) -> None:
        super().__init__(marca, modelo, ano)
        self.status = status

carro = Carro("Fiat", "147", 1980)