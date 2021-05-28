# Trabalho Grafos - Kruskal

## Algoritmo de Kruskal

O algoritmo de Kruskal é um algoritmo em teoria dos grafos que busca uma árvore geradora mínima para um grafo conexo com pesos. Isto significa que ele encontra um subconjunto das arestas que forma uma árvore que inclui todos os vértices, onde o peso total, dado pela soma dos pesos das arestas da árvore, é minimizado. Se o grafo não for conexo, então ele encontra uma floresta geradora mínima (uma árvore geradora mínima para cada componente conexo do grafo). 

Com o uso de uma estrutura de dados eficiente, o algoritmo de Kruskal possui complexidade de tempo igual a O (m log n), onde m representa o número de arestas e n o número de vértices.


## Tutorial

* Tenha o python instalado na maquina
* Crie um arquivo requirements.txt e cole os itens abaixo:<br />
tk<br />
matplotlib<br />
networkx<br />
* Execute o comando pip install -r requirements.txt
* Execute o arquivo KruskalFinal.py com python KruskalFinal.py


## Bibliotecas utilizadas no trabalho

### Matplotlib

É uma biblioteca de software para criação de gráficos e visualizações de dados em geral, feita para e da linguagem de programação Python.

### Tkinter
- Baseada em Tcl/Tk, a Tkinter acompanha a distribuição oficial do interpretador Python. É a biblioteca padrão da linguagem Python. Tanto o Tk quanto o tkinter estão disponíveis na maioria das plataformas Unix, bem como em sistemas Windows. (Tk em si não faz parte do Python; é mantido no ActiveState.)


### Networkx
NetworkX é uma biblioteca da linguagem de programação Python para estudar grafos e redes. NetworkX é um software livre lançado sob a licença BSD.

Características:

 * Classes para grafos não direcionados e direcionados.
 * Conversão entre formatos de grafos.
 * Capacidade de construir grafos aleatórios ou construí-los de forma incremental.
 * Capacidade de encontrar subgrafos, cliques e núcleos k.
 * Possibilita analisar adjacência, grau, diâmetro, centralidade, etc.
 * Desenhar redes em 2D e 3D.


## Corretude

Seja A(T) uma árvore geradora mínima de retorno do algoritmo de Kruskal e T(T*) uma árvore geradora mínima mais próxima de A, chegaremos a conclusão que A = T. Vamos assumir que A != T.

Considerando a sequencia e1,e2,...em e seja e = ei a primeira aresta que está em A e não está em T, sendo assim haverá um ciclo C de T + e, já que não há ciclos em A, há uma aresta x que pertence a E(C - e) que não existem em A, logo, x pertence E(T) - E(A).

Como x pertence E(T) - E(A), então x não pertence a e1,e2,...,ei. Então é w(e) <= w(x). 

Considerando uma árvore geradora M = T - x + e, logo w(M) <= w(T) e M  é uma árvore geradora mínima, contrariando a escolha de T, logo A é uma árvore geradora mínima.



[Link Apresentação Youtube](https://www.youtube.com/)
