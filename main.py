from models import Carro


carro = Carro("vermelho", "grande") # OBJETO

print(carro.abastecer(20))

carro.girar_chave()
print(carro.status)
carro.girar_chave()
print(carro.status)

a = carro.aceleracao(10, 10, 5, 2)
print(a)
a = carro.aceleracao(10, 10)

print(carro.__dict__)
