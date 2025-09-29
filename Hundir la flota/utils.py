import numpy as np 
import random
import time

# creacion de tableros

def crear_tablero(tamaño):
    import numpy as np
    tablero = np.full((tamaño, tamaño), "_")
    return tablero

# colocar barcos

def colocar_barco(barco, tablero):
    for fila, columna in barco:
        tablero[fila, columna] = "O"

# disparar 

def disparar(casilla, tablero):
    fila, columna = casilla 
    if tablero [fila, columna] == "O":
        tablero[fila,columna ] = "X"
        return "Tocado" 
    
    else:
        tablero[fila,columna] = "A"
        return "Agua"

# creacion de barcos

def crear_barco(eslora, tamaño_tablero = 10):
    import random
    orientacion = random.choice(["horizontal", "vertical"])
    
    if orientacion == "horizontal":
        fila = random.randint(0, tamaño_tablero -1)
        columna_inicial = random.randint(0, tamaño_tablero - eslora)
        barco = [(fila, columna_inicial + i) for i in range(eslora)]
    
    else:
        fila_inicial = random.randint(0, tamaño_tablero - eslora)
        columna = random.randint(0, tamaño_tablero -1)
        barco = [(fila_inicial + i, columna) for i in range(eslora)]
    
    return barco

# comprobacion de superposicion de barcos al crearse

def superposicion_barcos(uno, dos, tres, cuatro, cinco, seis):
    posiciones = []
    for barco in [uno, dos, tres, cuatro, cinco, seis]:
        for fila, columna in barco:
            if [fila, columna] in posiciones:
                return False
            posiciones.append([fila, columna])
    return True

# comprobacion de si quedan barcos vivos en los tableros

def quedan_barcos(tablero):
    for fila in tablero:
        if "O" in fila:
            return True
    return False
