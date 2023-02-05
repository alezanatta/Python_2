from typing import Text
import os
import re
import operator
from constantes import CABECALHO, ESPACOS, CASAS_DECIMAIS, DIVISAO_BIT


class Relatorio():
    def __init__(self, arquivo: Text, id=False) -> None:
        self.url_arquivo = arquivo
        self._le_arquivo()
        if id:
            self.id = self._separador("^[0-9]{1,5}")
        else:
            self.id = None
        self.esp_utilizado = self._separador("[0-9]+$")
        self.funcionarios = self._separador("[a-z]+[ ]?[a-z]+", re.IGNORECASE)
        self.converte()
        self.total_utilizado()
        self._media_usuario()
        self.porcentagem_uso()
        #  Preciso saber se é extremamente errado chamar os métodos na própria inicialização

    @staticmethod
    def _alinhamento(arg) -> str:
        return str(arg).ljust(ESPACOS)

    def _dicio(self, arg) -> list:
        dic = {}
        for x, i in enumerate(self.funcionarios):
            dic.update({i: (arg[x])})
        sorted_d = sorted(dic.items(), key=operator.itemgetter(1))
        return sorted_d

    def _corpo(self) -> None:
        if self.id:
            for x in range(0, len(self.funcionarios)):
                print((self._alinhamento(self.id[x])) +
                      self._alinhamento(self.funcionarios[x]) +
                      self._alinhamento(self.convertido[x]) +
                      self._alinhamento(self.porcentagem[x]))
        else:
            for x in range(0, len(self.funcionarios)):
                print((self._alinhamento(x + 1)) +
                      # + 1 para corrigir numero do Id
                      self._alinhamento(self.funcionarios[x]) +
                      self._alinhamento(self.convertido[x]) +
                      self._alinhamento(self.porcentagem[x]))

    def _le_arquivo(self) -> list:
        base = os.getcwd()
        arquivo = open(os.path.join(f"{base}", self.url_arquivo), "r")
        self.conteudo = arquivo.readlines()
        arquivo.close()
        return self.conteudo

    def _separador(self, pattern: str, flag=False) -> list:
        temp = []
        for linha in self.conteudo:
            if flag:
                match = re.findall(pattern, linha, flag)
            else:
                match = re.findall(pattern, linha)
            match = "".join(match)
            temp.append(match)
        return temp

    def _media_usuario(self) -> None:
        self.media = round(self.total / len(self.funcionarios), CASAS_DECIMAIS)

    def converte(self, data="MB") -> list:
        self.convertido = []
        if data == "MB":
            for i in self.esp_utilizado:
                self.convertido.append(round(float(i) / DIVISAO_BIT, CASAS_DECIMAIS))
        return self._dicio(self.convertido)
        # implementar conversões além de MB

    def porcentagem_uso(self) -> list:
        self.porcentagem = []
        for i in self.convertido:
            self.porcentagem.append(round(i / (self.total / 100), CASAS_DECIMAIS))
        return self._dicio(self.porcentagem)

    def total_utilizado(self) -> int:
        self.total = sum(self.convertido)
        return self.total

    def imprime_relatorio(self) -> None:
        print(CABECALHO)
        self._corpo()
        print(f"Espaço total ocupado: {self.total} MB\n" f"Espaço médio ocupado: {self.media} MB")

    def colunas(self, arg: str) -> list:
        arg = arg.lower()
        if arg == "usuario":
            return sorted(self.funcionarios)
        elif arg == "uso":
            return self.esp_utilizado  # Tentando achar uma maneira de transformar em int (sem usar for), para poder colocar em ordem crescente
        elif arg == "porcentagem":
            return self.porcentagem  # Tentando achar uma maneira de transformar em int (sem usar for), para poder colocar em ordem crescente
