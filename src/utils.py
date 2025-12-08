def EstadoInicial(G): #Esta funcion crea un estado inicial aleatorio
    estados=[randint(0,1) for i in srange(G.order())]
    return estados

def HacerDicCol(estados): #Esta funcion crea un diccionario para colorear la gráfica a partir del estado de los vértices
    ceros=[]
    unos=[]
    dos=[]
    for i in srange(len(estados)):
        if estados[i]==0:
            ceros.append(i)
        if estados[i]==1:
            unos.append(i)
        if estados[i]==2:
            dos.append(i)
    d={'white':ceros, 'red':unos, 'black':dos } #d={'cyan':ceros, 'red':unos, 'purple':dos }
    return d

def Rejilla(n,m): # Esta funcón crea una rejilla
    G=Graph()
    contador=0
    for i in srange(n):# Este for enumera los vertices
        for j in srange(m):
            G.add_vertex(contador)
            contador=contador+1
    verticales=[[a,b] for a in G.vertices() for b in G.vertices() if a-b==n] #aristas verticales
    horizontales=[[a,b] for a in G.vertices() for b in G.vertices() if b-a==1 and b%n!=0] #aristas horizontales
    G.add_edges(verticales)
    G.add_edges(horizontales)
    return G