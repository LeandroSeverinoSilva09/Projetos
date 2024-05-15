import pandas as pd
import os

dir = os.getcwd()
print (dir)
nome_da_planilha = input("Digite o nome da planilha: ")
caminho_planilha1 = dir + "//" +  nome_da_planilha
nome_aba_p1 = input("Digite o nome da Página que deseja extrair a coluna: ")
nome_da_coluna_p1 = input("Digite o nome da da coluna: ")
dados_p1 = pd.read_excel(caminho_planilha1, sheet_name=nome_aba_p1, usecols=[nome_da_coluna_p1], header=5)
lista_valores_plan1 = dados_p1[nome_da_coluna_p1].tolist()
print (lista_valores_plan1)
with open (dir + "//resultado.txt" , 'w') as arquivo:
    arquivo.write(str(lista_valores_plan1))


