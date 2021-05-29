from collections import defaultdict
from dataclasses import dataclass
import networkx as nx
import matplotlib
from networkx.algorithms.shortest_paths import weighted
from tkinter import messagebox
import matplotlib.pyplot as plt
from collections import OrderedDict
import tkinter as tk
from tkinter import *

from networkx.classes.function import is_empty

#Verifico qual o valor da chave v se for igual eu retorno o valor, caso não seja, entro na recursão 
#para achar o valor do v inicial 
def Compara(v):
    #Verifica se a chave é igual ao valor
    if vetor[v] != v:
        #Atribui à chave o valor 
        vetor[v] = Compara(vetor[v])
    return vetor[v]


def criarDesenhoGrafo(conexaoresultado,custo):
    #Inicia o grafo no networkx e adicionar as conexoes no vetor peso
    g = nx.Graph()
    pesos = []
    for val in conexaoresultado:
        pesos.append((val[1],val[2],val[0]))

    #Adiciona conexoes ao grafo e define layout
    g.add_weighted_edges_from(pesos)
    pos=nx.spring_layout(g)

    #Cria o desenho com rótulos e valores de peso das arestas
    nx.draw(g, pos, with_labels=True, font_weight='bold')
    peso_arestas = nx.get_edge_attributes(g,'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels = peso_arestas)

    #Adiciona ao plot o texto com a informação do custo mínimo
    plt.suptitle("Custo Mínimo: "+str(custo))
    #Exibe o plot
    plt.show()
  


def gerarGrafo():

    #Cria as conexões com vértice e arestas vazias
    conexoes = {'V': [],'E': []}
    
    #Insere em conexões['V'] os vértices sem repetir e as conexões (peso,verticex, verticey) em conexoes['E'] 
    for i,val in enumerate(entradas):
        if(val[1] not in conexoes['V']):
            conexoes['V'].append(val[1])
        if(val[2] not in conexoes['V']):
            conexoes['V'].append(val[2])
        conexoes['E'].append(val)
    
   
    #Adiciono em chave e valor o rótulo dos vértices e conto quantos vértices tem
    cont = 0
    while(cont < len(conexoes['V'])):
        vetor[conexoes['V'][cont]] = conexoes['V'][cont]
        cont = cont + 1
    
    #Faço a ordenação das conexoes por pesos
    arestas = list(conexoes['E'])
    arestas.sort()
    
    peso_arvore = 0
    arvore = []

    for conexao in arestas:
        peso, u, v = conexao

        #Comparação que Analisa se a aresta forma um ciclo, caso não forme adiciono na árvore a conexão,
        #pois se forem iguais já existem 2 valores iguais para as duas chaves passadas como parametro, logo um ciclo
        #seria formado

        if Compara(u) != Compara(v):
            arvore.append(conexao)
            #É realizada a ligação entre os vértices através de atribuições para que caso duas chaves 
            #tenham um mesmo valor um ciclo seja impedido de ser formado atraves da função compara
            for conexao in arestas:
                vetor[Compara(u)] = Compara(v)

    # Somo os pesos da árvore
    for conexao in arvore:
        peso, u, v = conexao
        peso_arvore += peso
    
    #Chamo o metódo para desenhar e exibir o grafo
    criarDesenhoGrafo(arvore,peso_arvore)

def limpar():
    #Limpa o vetor de entradas
    entradas.clear()
    #Destrói os itens do frame que mostra as conexões adicionadas
    for widget in frame_b.winfo_children():
        widget.destroy()
    vetor.clear()

def adicionarConexao():
    #Caso algum dos campos não sejam preenchidos, gerar uma exceção solicitando o preenchimento de todos os campos
    if(e1.get() == "" or e2.get() == "" or e3.get() == ""):
        messagebox.showwarning('Atenção','Por favor preencha todos os campos')
    #Caso o campo peso seja preenchido com letras, gerar uma exceção solicitando que o campo seja preenchido corretamente
    elif(e3.get().isdigit() == False):
        messagebox.showwarning('Atenção','O campo de peso deve ser preenchido com um número')
    else:
        messagebox.showinfo('Sucesso','Conexão Adicionada!')
        #Substituindo virgulas por pontos caso a entrada passada pelo usuario com virgula, 
        #pois o tipo float não reconhece virgulas
        peso_replaced = e3.get().replace(",", ".")
        #Adicionando a conexão no vetor de entradas
        entradas.append((float(peso_replaced),e1.get(),e2.get()))
        #Limpando e adicionando a label do frame_b  o texto que mostra quais 
        # conexões já foram adicionadas anteriormente. 
        texto = ""
        texto = "Peso = " + str(peso_replaced) + " | Vértice x = " + str(e1.get()) + " | Vértice y = " + str(e2.get())
        tk.Label(master=frame_b, text= texto).grid(row=4*len(entradas))
        # Limpa os valores digitados nos 3 inputs
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)


#Inicio do programa
entradas = []
vetor = dict()
linha = 4

#Criando a janela e 2 frames, onde um frame vai conter as entradas e botões 
# e o outro frame as conexões adicionadas
window = tk.Tk()
frame_a = tk.Frame()
frame_b = tk.Frame()

#Criando labels no frame_a
tk.Label(master=frame_a, text="Vértice x").grid(row=0)
tk.Label(master=frame_a, text="Vértice y").grid(row=1)
tk.Label(master=frame_a, text="Peso da aresta").grid(row=2)

#Criação de inputs
e1 = tk.Entry(master=frame_a)
e2 = tk.Entry(master=frame_a)
e3 = tk.Entry(master=frame_a)

#Definindo a localização dos inputs
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

#Botão que chama o metodo limpar()
tk.Button(master=frame_a, text='Limpar', command=limpar).grid(row=3, 
                                                                column=0, 
                                                                sticky=tk.W, 
                                                                pady=0)     
#Botão que chama o metodo adicionarConexao()
tk.Button(master=frame_a, text='Adicionar Conexão', command=adicionarConexao).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=0)        
#Botão que chama o metodo gerarGrafo()                                           
tk.Button(master=frame_a, text='Gerar Grafo', command=gerarGrafo).grid(row=3, 
                                                                column=2, 
                                                                sticky=tk.W, 
                                                                pady=0)
#Setando o titulo da aplicação
window.title("Kruskal")
#Empacotando os frames
frame_a.pack()
frame_b.pack()
#Definindo o tamanho da janela
window.geometry('500x400')

#Método que permite que o Tkinter comece a executar o aplicativo. 
#Faz um loop indefinido até que o usuário saia da janela ou aguarde qualquer evento do usuário. 
window.mainloop()







