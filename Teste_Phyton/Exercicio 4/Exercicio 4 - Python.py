from cmath import nan
from pandas import read_excel, DataFrame, ExcelWriter
from datetime import datetime
import time

#A única informação disponível para que essa troca seja possível são
#os horários de início e término de uso de cada licença
path_file1 = ".\\Input_Teste_Python_Dados Exercicio 4 I.xlsx"
path_file2 = ".\\Input_Teste_Python_Dados Exercício 4 II.xlsx"
sheetName = "Sheet1"

print("Lendo os datasets...")

data_no_user = read_excel(path_file1, sheetName)
data_with_user = read_excel(path_file2, sheetName)


print("Vetorizando os dados...")
# Vetorizando os dados para dividir as tarefas
tempo_inicial1 = time.time()

noUser_StartTime = data_no_user['Start Time']
noUser_EndtTime = data_no_user['End Time']
withUser_Hinicio = data_with_user['Hora Inicio']
withUser_Htermino = data_with_user['Hora Termino']
withUser_Dinicio = data_with_user['Data Inicio']
withUser_DTermino = data_with_user['Data Termino']

tempo_final1 = time.time()
tempo_final1 -= tempo_inicial1



print("Concatenando os dados de Start Time + Hora Inicio e End Time + Hora Termino...")
withUser_StartTime = []
withUser_EndTime = []

tempo_inicial2 = time.time()
# setando todos os starttime e endtime da planilha com os usuarios
for w_Dinicio, w_Hinicio, w_Dtermino, w_Htermino in zip(withUser_Dinicio, withUser_Hinicio, withUser_DTermino, withUser_Htermino):
    withUser_StartTime.append(str(w_Dinicio)+" "+str(w_Hinicio))
    withUser_EndTime.append(str(w_Dtermino)+" "+str(w_Htermino))

tempo_final2 = time.time()
tempo_final2 -= tempo_inicial2

# modo de formatacao dos dados
# noUser_StartTime -> dd/mm/yyyy hh:mm
# withUser_StartTime -> yyyy-mm-dd hh:mm
# 

withUser_Usuario = data_with_user['Usuario']
UsuariosEncontrados_dadosSaida = []
UsuariosNaoEncontrados_dadosSaida = []

print("Cruzando os dados...")
tempo_inicial3 = time.time()

for i in range(len(withUser_StartTime)):
    for j in range(len(noUser_StartTime)):
        #se o end time da planilha que contem o usuario for nan, entao nao precisa
        #verificar os proximos passos
        if('nan' in withUser_EndTime[i]):
            UsuariosNaoEncontrados_dadosSaida.append([withUser_Usuario[i], withUser_StartTime[i], ""])
            break
        #precisamos fazer essa conversão pois os formatos divergem nos dados
        nU_dataInicio = datetime.strptime(noUser_StartTime[j], "%d/%m/%Y %H:%M")
        w_dataInicio= datetime.strptime(withUser_StartTime[i], "%Y-%m-%d %H:%M")
        #comparando entao se as datas de inicio e termino coincidem 
        if nU_dataInicio == w_dataInicio and withUser_EndTime[i] == noUser_EndtTime[j]:
            UsuariosEncontrados_dadosSaida.append([withUser_Usuario[i], noUser_StartTime[j], noUser_EndtTime[j]])

tempo_final3 = time.time()
tempo_final3 -= tempo_inicial3

Encontrados_dadosSaida = DataFrame(UsuariosEncontrados_dadosSaida, columns=['Usuario', 'Hora Inicial', 'Hora Final'])
NaoEncontrados_dadosSaida = DataFrame(UsuariosNaoEncontrados_dadosSaida, columns=['Usuario', 'Hora Inicial', 'Hora Final'])

print("Criando os arquivos...")
#criando arquivo na pasta
arquivo = ExcelWriter('dadosDeSaida - Exercicio 4.xlsx')
with ExcelWriter('.\\dadosDeSaida - Exercicio 4.xlsx') as writer:
    Encontrados_dadosSaida.to_excel(writer, sheet_name="Finalizados")
    NaoEncontrados_dadosSaida.to_excel(writer, sheet_name="Em execução")
arquivo.close

print("Finalizado.")
print(f"Tempo total de execução dos algoritmos utilizados: {tempo_final1+tempo_final2+tempo_final3} segundos")


