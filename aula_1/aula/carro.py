class Carro:  # CLASSE

    def __init__(self, cor: str, tamanho: str) -> None:
        self.cor = cor
        self.tamanho = tamanho
        self.litros = 0
        self.status = "Desligado"
        self.velocidade = 0
        # ATRIBUTOS

    def girar_chave(self):
        if self.status == "Ligado":
            self.status = "Desligado"
        elif self.status == "Desligado":
            self.status = "Ligado"
        else:
            self.status = "Pane"


    def abastecer(self, litros_abastecer: int) -> str:  # MÉTODO
        preco = 10  # valor
        valor = preco * litros_abastecer
        self.litros += litros_abastecer
        return (f"Preço: {valor}, litros atuais: {self.litros}")

    def aceleracao(self, velocidadeFinal, tempoFinal, velocidadeInicial = 0, tempoInicial = 0) -> float:  # MÉTODO
        velocidade = velocidadeFinal - velocidadeInicial
        tempo = tempoFinal - tempoInicial
        aceleracao = velocidade / tempo
        self.velocidade = velocidade
        return aceleracao