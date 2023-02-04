from typing import Union


class Carro:

    def __init__(self,
                 marca: str,
                 modelo: str,
                 ano: Union[int, None] = None) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


carro = Carro("Fiat", "147", 1980)
