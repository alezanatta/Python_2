from manipula import Manipula
from classes import Funcionario


manip = Manipula("func.txt", Funcionario)

manip.arquivo_setter("Jonas,Gerente,1200")  # Adicionando linha no arquivo
manip.arquivo_delete("Jonas")  # Deletando a linha que o nome Jonas aparece
func = manip.arquivo_getter()  # Pegando objetos do arquivo
for funcionario in func:  # Mostrando na tela as informações dos objetos
    print(funcionario)

manip.compacta()  # Compactando arquivo para Zip


# Conteudo inicial do arquivo
"""Joao Pereira,Gerente,3000
Joana,Funcionario generico,500
Joaninha,Funcionario generico,1200"""
