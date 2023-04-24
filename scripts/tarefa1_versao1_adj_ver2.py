# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 10:51:49 2023

@author: maria
"""

ficheiro_input="input_01.txt"
ficheiro_dicionario=  "mini_dic.txt" # "mini_dic.txt"

import time
tempo_inicial=time.time()

from binary_search import binary_search

def adj(pal1, pal2): #ve se fuas palavras sao adjuntas
    count=0
    if(pal1==pal2):
        return False
    
    for i in range(len(pal1)):#sao adjacentes se alterando uma unica letra a uma delas se tornarem iguais 
        if(pal1[i]!=pal2[i]):
            count+=1  
            if(count>1): #se for necessario alterar mais de 1 entao nao sao adjacentes 
                return False
    return True       

def adicionaAresta(grafo,u,v):
    grafo[u].append(v)
    grafo[v].append(u)

# Procura em largura (devolve o menor n'umero de arestas entre v_origem e v_destino ou -1, caso não exista um caminho entre v_origem e v_destino)
def bfs(n, grafo, v_origem, v_destino):
    # cria lista dos vértives visitados (inicializada a False)
    visitado = [False] * n
    # cria uma lista que guarda, para cada vértice v, o menor número de arestas entre v_origem e v (inicializada a infinito).
    dist = [float('inf')] * n
    fila = []
    fila.append(v_origem)
    visitado[v_origem] = True
    dist[v_origem]=0
 
    while fila:
        u = fila.pop(0)
        for v in grafo[u]:
            if visitado[v] == False:
                fila.append(v)
                visitado[v] = True
                dist[v]=dist[u]+1
                if v == v_destino:
                    return dist
    return -1

#ler input
f_in = open(ficheiro_input, "r")


pals_ab= f_in.readlines()
for i in range(len(pals_ab)):
    pals_ab[i]=pals_ab[i].split(" ")
    if(i!= len(pals_ab)-1):
        pals_ab[i][1] = pals_ab[i][1][:-1]
    else:
        pals_ab[i][1] = pals_ab[i][1]

#print("Pares de palavras input:" ,pals_ab)  
#ver numero de comprimento de palavras necessario

comprimentos=[]
for i in pals_ab:
    comprimentos.append( len(i[0]))

#print("Comprimentos:", comprimentos)
comprimentos= list(set(comprimentos))
#print(comprimentos)

#ler ficheiro dicionario
f_di = open(ficheiro_dicionario , "r")

dicionario = f_di.readlines()
for i in range(len(dicionario)):
    dicionario[i]=dicionario[i][:-1]
    
dicionario= list(set(dicionario))
#print("Dicionario:", dicionario, "\n")

#definir lista ordenada para cada comprimento de palavras
keys=comprimentos
values= [[] for i in range(len(keys))]
grafos=[]

for palavra in dicionario:
    if(len(palavra) in keys):
        ind_k = keys.index(len(palavra))
        values[ind_k].append(palavra)

  
for i in range(len(values)):
    values[i]= sorted(values[i])

my_dict = dict(zip(keys,values))
print("Dicionario pyhton:",my_dict, "\n")

tempo_ate_dic=time.time()
print("Tempo de execução ate fim dicionario = ",tempo_ate_dic - tempo_inicial, "segundos")

for comprimento in my_dict: #um grafo para cada conjunto de palavras com o mesmo comprimento 
    palavras=my_dict[comprimento]
    n=len(palavras) #numero de vertices
    grafo = [[] for i in range(n)] # O grafo é representado por uma lista de adjacências.
    #Cada posição i da lista grafo contém uma lista com os vértices adjacentes ao vértice i.
    for j in range(n): #para cada palavra 
        for k in range(j+1, n): #comparar com as restantes palavras ainda nao comparadas
            if(adj(palavras[j],palavras[k])): #se palavras adjacentes = 1 letra de diferença
                adicionaAresta(grafo, j, k)  #entao ha uma aresta entre as palavras
    #print("key:", comprimento, "dict:", my_dict[comprimento])
    #print("Grafo:", grafo)
    grafos.append(grafo)
    
my_grafos = dict(zip(keys,grafos))

tempo_ate_graf=time.time()

print("Tempo de execução de formaçao grafos = ",tempo_ate_graf - tempo_ate_dic, "segundos", (tempo_ate_graf - tempo_ate_dic)/60, "minutos")
print("Tempo de execução ate fim formaçao grafos = ",tempo_ate_graf - tempo_inicial, "segundos", (tempo_ate_graf - tempo_inicial)/60, "minutos")

for i in pals_ab: #para cada par i 
    pala=i[0]
    palb=i[1]
    if(binary_search(my_dict[len(pala)], 0, len(my_dict[len(pala)])-1, pala)==-1 or 
       binary_search(my_dict[len(pala)], 0, len(my_dict[len(pala)])-1, pala)==-1):
        print(pala, "-1")
        print(palb, "\n")
        
    elif(pala==palb):
        print(i[0], "0")
        print(i[1], "\n")
    
    else:
        dici = my_dict[len(pala)]    
        v1 =  dici.index(pala)
        v2 = dici.index(palb)
        n=len(dici)
        grafo= my_grafos[len(pala)]
        result= bfs(n, grafo, v1,v2)
        if(result==-1):
            print(pala, result)
            print(palb, "\n")
        else:
            dici = my_dict[len(pala)]    
            v1 =  dici.index(pala)
            v2 = dici.index(palb)
            n=len(dici)
            grafo= my_grafos[len(pala)]
            r1= bfs(n, grafo, v1,v2)
            p=r1
            if(p==-1):
                print(pala, p)
                print(palb, "\n")
            else: #incompleto, nao vai ser o mesmo no futuro
                r2= bfs(n, grafo, v2,v1)
                
                maxv=0
                for i in range(len(r1)):
                    if(r1[i]!= float('inf') and maxv < r1[i]):
                        maxv=r1[i]
    
                for i in range(len(r1)):
                    if(r1[i]!=maxv-r2[i]):
                        r1[i]=-1
                
                print(pala, maxv)
                for i in range(1,maxv):
                    elem=r1.index(i)
                    print(dici[elem])
                print(palb, "\n")

tempo_final=time.time()

print("Tempo de execução = ",tempo_final - tempo_inicial, "segundos = ", (tempo_final - tempo_inicial)/60, "minutos" )
