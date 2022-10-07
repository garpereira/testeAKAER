n_pecas = int(input("Quantas pecas joaozinho tem?\nR: "))
lista_pecas = []
for i in range(1,n_pecas):
    lista_pecas.append(int(input(f"Qual o valor da peca {i}: "))) 

resultado = 0
lista_pecas.sort()
for i in range(0,n_pecas):
    if(lista_pecas[i] != i+1):
        resultado = i+1
        break
print(f"Joaozinho deve pedir a peca {resultado}")

