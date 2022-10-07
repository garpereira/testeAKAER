# import pandas as pd
from pandas import read_excel, DataFrame
from datetime import datetime
import time

def diferenca_datas(startTime, endTime):
  #convertendo a string para um objeto do tipo data
  day1 = datetime.strptime(startTime, "%d/%m/%Y %H:%M")
  day2 = datetime.strptime(endTime, "%Y-%m-%d %H:%M:%S")
  diferenca = day2 - day1
  return diferenca


print("Lendo o dataset...")
path_file = ".\\Input_Teste_Python_exercicio 3.xlsx"
sheetName = "Sheet1"
data = read_excel(path_file, sheet_name=sheetName)

#agrupando os dados de acordo com as colunas de interesse

#seria possivel realizar os agrupamentos utilizando de vetores auxiliares, ou seja, 
#uma lista para cada coluna de interesse, realizando então uma iteração considerando
#iguais indices para cada lista obtendo o mesmo resultado, porém a fim de otimização
#de uso da memória disponível, optei pelo uso da função groupby da biblioteca pandas
#para este fim, já que realiza esta mesma função sem a utilização de 4*[n] espaços
# extras de memória

print("Agrupando os dados das colunas 'User Name', 'Start Time', 'End Time', 'License Type'...")
tempo_inicial0 = time.time()

agrupados = data.groupby(["User Name", "Start Time", "End Time", "License Type"])

tempo_final0 = time.time()
tempo_final0 -= tempo_inicial0

print("Criando a lista com as informações obtidas com o agrupamento...")
# criando uma lista de listas com cada informação obtida
GrupoDados = []
tempo_inicial1 = time.time()

for key, item in agrupados:
    GrupoDados.append(list(key))

tempo_final1 = time.time()
tempo_final1 -= tempo_inicial1
#liberando memoria
agrupados = 0

dados_deSaida = []

print("Criando a lista com os calculos de horas...")
tempo_inicial2 = time.time()

for item in GrupoDados:
    #guardando a linha inteira de dados
    auxiliar = list(item)
    #alterando as ordens dos itens para ficar de acordo com o pdf
    auxiliar[1] = item[3] #license type
    auxiliar[2] = item[1] #date
    #calculando a diferenca de horas das datas observadas
    auxiliar[3] = str(diferenca_datas(item[1], item[2]))
    dados_deSaida.append(auxiliar)

tempo_final2 = time.time()
tempo_final2 -= tempo_inicial2
#liberando memoria
GrupoDados = 0

print("Criando o arquivo de saida...")
#gerando xlsx com os dados gerados
GrupoDados = DataFrame(dados_deSaida, columns=['Usuario', 'Licença', 'Dia', 'Tempo de Uso'])
GrupoDados.to_excel('dadosDeSaida - Exercicio 3.xlsx', sheet_name='Sheet1')

print("Finalizado.")
print(f"Tempo total de execução dos algoritmos utilizados: {tempo_final0+tempo_final1+tempo_final2} segundos")