from exercicio import Relatorio


relatorio = Relatorio("usuarios.txt")
#relatorio = Relatorio("usuarios2.txt", id=True)
"""usuarios.txt > não possue id na frente,
   o id fica em ordem crescente como padrão
   usuarios2.txt > seria uma situação que supostamente
   somente alguns usuarios de id especifico fossem selecionados   """

relatorio.imprime_relatorio()

print(relatorio.converte())
print(relatorio.porcentagem_uso())
print(relatorio.colunas("uso"))
print(relatorio.colunas("usuario"))
print(relatorio.colunas("porcentagem"))
