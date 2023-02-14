import os
from zipfile import ZipFile


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

def abrir_arquivo(arquivo, modo):
    arquivo = open(os.path.join(BASE_DIR, arquivo), f"{modo}")
    return arquivo

class Manipula:
    def __init__(self, arquivo, objeto) -> None:
        self.arquivo = arquivo
        self.objeto = objeto

    def arquivo_setter(self, conteudo) -> None:
        arquivo = abrir_arquivo(self.arquivo, "a")
        arquivo.write(conteudo + "\n")
        arquivo.close()

    def arquivo_getter(self): # Esta correto devolver 1 objeto para cada linha do arquivo?
        arquivo = abrir_arquivo(self.arquivo, "r")
        objetos = []
        for linha in arquivo:
            linha = linha.replace("\n", "").split(",")
            objeto = self.objeto(*linha)
            objetos.append(objeto)
        arquivo.close()
        return objetos

    def arquivo_delete(self, nome):
        arquivo = abrir_arquivo(self.arquivo, "r")
        conteudo = []
        for linha in arquivo:
            linha = linha.split(",")
            if nome in linha:
                continue
            conteudo.append(linha)
        arquivo.close()
        arquivo = abrir_arquivo(self.arquivo, "w")  #implementar arquivo temporario para não ter risco de corromper
        for y in conteudo:
            y = ",".join(y)
            arquivo.write(y)
        arquivo.close()
        return

    def compacta(self): # Foi a maneira que consegui implementar o compactamento
        zipped = ZipFile(f"{self.arquivo}.zip", "w")
        for root, dirs, files in os.walk(BASE_DIR):
            for file in files:
                if self.arquivo in file.split("/"):
                    zipped.write(os.path.relpath(os.path.join(root, file)))
        return 
