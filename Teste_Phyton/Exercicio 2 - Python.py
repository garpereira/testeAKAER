n_botas  = int(input("Quantas botas contem nas caixas?\nR: "))
numeros = []
lados_pe = []
n_pares = 0

print("Digite agora os numeros das botas com seu lado do pe\n")
for i in range(0,n_botas):
    x = input(f"Digite tamanho e o lado do pe da bota {i+1}\nR: ").split()
    numeros.append(x[0])
    lados_pe.append(x[1])

for i in range(len(numeros)):
    for j in range(len(lados_pe)):
        if(numeros[i] == numeros[j] and lados_pe[i] != lados_pe[j]):
            n_pares += 1
            numeros[i] = 0
            numeros[j] = 0
            lados_pe[i] = 0
            lados_pe[j] = 0

print(f"O numero de pares possiveis sao: {n_pares}")
            
# 4
# 40 D
# 41 E
# 41 D
# 40 E
