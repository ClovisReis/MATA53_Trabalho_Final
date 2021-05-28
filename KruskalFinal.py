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



def Compara(vertice):
    if vetor[vertice] != vertice:
        vetor[vertice] = Compara(vetor[vertice])
    return vetor[vertice]


def geraGrafo(conexaoresultado,custo):
    g = nx.Graph()
    #print(conexaoresultado)
    pesos = []
    for val in conexaoresultado:
        pesos.append((val[1],val[2],val[0]))
    #print(pesos)
    #for val in conexaoresultado:
    g.add_weighted_edges_from(pesos)
    pos=nx.spring_layout(g)
    #f = plt.text("teste","testando").figure()
    
    #f = plt.figure()
    
    nx.draw(g, pos, with_labels=True, font_weight='bold')
    peso_arestas = nx.get_edge_attributes(g,'weight')
    nx.draw_networkx_edge_labels(g, pos, edge_labels = peso_arestas)
    #g.add_edge(val.v1,val.v2, weight=val.peso)
    
    
    #nx.draw(g, with_labels=True)
    plt.suptitle("Custo Mínimo :"+str(custo))
    
    plt.show()
    #f.savefig("conexoes.png")


def tratamentoEntrada():

    conexoes = {'V': [],'E': []}
    for i,val in enumerate(entradas):
        if(val[1] not in conexoes['V']):
            conexoes['V'].append(val[1])
        if(val[2] not in conexoes['V']):
            conexoes['V'].append(val[2])
        conexoes['E'].append(val)
    
   

    cont = 0
    while(cont < len(conexoes['V'])):
        vetor[conexoes['V'][cont]] = conexoes['V'][cont]
        cont = cont + 1

    arestas = list(conexoes['E'])
    arestas.sort()
    peso_arvore = 0
    arvore = []

    for conexao in arestas:
        peso, u, v = conexao
        
        if Compara(u) != Compara(v):
            arvore.append(conexao)
            if Compara(u) != Compara(v):
                for conexao in arestas:
                    vetor[Compara(u)] = Compara(v)

    
    for conexao in arvore:
        peso, u, v = conexao
        peso_arvore += peso
    
    geraGrafo(arvore,peso_arvore)



def limpar():
    #print(entradas)
    entradas.clear()
    #print(entradas)
    for widget in frame_b.winfo_children():
        widget.destroy()

def arrumarEntradas():





    messagebox.showinfo('Sucesso','Conexão Adicionada!')

    peso_replaced = e3.get().replace(",", ".")
    entradas.append((float(peso_replaced),e1.get(),e2.get()))
    texto = ""

    texto = "Peso = " + str(peso_replaced) + " | Vértice x = " + str(e1.get()) + " | Vértice y = " + str(e2.get())
    tk.Label(master=frame_b, text= texto).grid(row=4*len(entradas))
    
    
    #print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)
    e3.delete(0, tk.END)


entradas = []
vetor = dict()
linha = 4

window = tk.Tk()
frame_a = tk.Frame()
frame_b = tk.Frame()

tk.Label(master=frame_a, text="Vértice x").grid(row=0)
tk.Label(master=frame_a, text="Vértice y").grid(row=1)
tk.Label(master=frame_a, text="Peso da aresta").grid(row=2)

e1 = tk.Entry(master=frame_a)
e2 = tk.Entry(master=frame_a)
e3 = tk.Entry(master=frame_a)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)


tk.Button(master=frame_a, text='Limpar', command=limpar).grid(row=3, 
                                                                column=0, 
                                                                sticky=tk.W, 
                                                                pady=0)     
tk.Button(master=frame_a, text='Adicionar Conexão', command=arrumarEntradas).grid(row=3, 
                                                               column=1, 
                                                               sticky=tk.W, 
                                                               pady=0)                                                     
tk.Button(master=frame_a, text='Gerar Grafo', command=tratamentoEntrada).grid(row=3, 
                                                                column=2, 
                                                                sticky=tk.W, 
                                                                pady=0)
window.title("Kruskal")
frame_a.pack()
frame_b.pack()
window.geometry('500x400')
window.mainloop()






