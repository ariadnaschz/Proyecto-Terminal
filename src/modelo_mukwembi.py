def Paso(G, estado, R): # Esta función hace un paso de tiempo de acuerdo con las reglas del autómata celular
    nuevoestado = estado[:]
    for i in srange(len(estado)):
        if estado[i] == 0:
            # Un vértice en estado 0 pasa a 1 si tiene al menos un vecino en estado 1
            if any(estado[vecino] == 1 for vecino in G.neighbors(i)):
                nuevoestado[i] = 1
        if estado[i] == 1:
            # Un vértice en estado 1 pasa a estar en estado 2
            nuevoestado[i] = 2
        if estado[i] == 2:
            # Un vértice en estado 2 pasa a 1 si tiene al menos R vecinos enfermos, de lo contrario será 0
            vecinos_enfermos = sum(1 for vecino in G.neighbors(i) if estado[vecino] == 1) 
            if vecinos_enfermos >= R:
                nuevoestado[i] = 1
            if vecinos_enfermos < R:
                nuevoestado[i] = 0
    return nuevoestado