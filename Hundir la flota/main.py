#importo todas las funciones creadas
from utils import *
import numpy as np 
import random
import time


#creo mi tablero y el de la maquina
tablero_propio = crear_tablero(10)
tablero_maquina = crear_tablero(10)

#creo seis barcos dentro de un bucle while True, en el que compruebo que no se superpongan.
#lo hago a través de uan fx que creé
#una vez que la fx dé True, avanza el programa

while True:
    uno = crear_barco(2)
    dos = crear_barco(2)
    tres = crear_barco(2)
    cuatro = crear_barco(3)
    cinco = crear_barco(3)
    seis = crear_barco(4)
    if superposicion_barcos(uno, dos, tres, cuatro, cinco, seis):
        break

#los coloco "manualmente" en mi tablero

colocar_barco((uno), tablero_propio)
colocar_barco((dos), tablero_propio)
colocar_barco((tres), tablero_propio)
colocar_barco((cuatro), tablero_propio)
colocar_barco((cinco), tablero_propio)
colocar_barco((seis), tablero_propio)

#hago lo mismo con los barcos de la maquina y los coloco "manualmente" en su tablero
#se sobreescriben las variables "uno", "dos", "tres"... pero no afecta a mi tabla creada
#como no hay que volver a utilizar esas variables originales, entiendo que no hay problema

while True:
    uno = crear_barco(2)
    dos = crear_barco(2)
    tres = crear_barco(2)
    cuatro = crear_barco(3)
    cinco = crear_barco(3)
    seis = crear_barco(4)
    if superposicion_barcos(uno, dos, tres, cuatro, cinco, seis):
        break

colocar_barco((uno), tablero_maquina)
colocar_barco((dos), tablero_maquina)
colocar_barco((tres), tablero_maquina)
colocar_barco((cuatro), tablero_maquina)
colocar_barco((cinco), tablero_maquina)
colocar_barco((seis), tablero_maquina)

#podría haber encontrado maneras más pragmáticas de crear barcos y comprobar si se superponían en el tablero, hay mucho código repetido

#imprimo solamente mi tablero, no el de la maquina
print("Este es tu tablero. ¡A jugar!")
time.sleep(1) #pausa y se imprime el tablero
print(tablero_propio)


#empiezan los bucles while a partir de aquí que siguen la lógica del juego

intentos = 10 # limito a 10 intentos para que no sea un juego muy largo

# bucle while con tres condiciones que se deben cumplir para mantener la dinámica del juego
# utilizo una funcion creada que comprueba si hay "O" en ambas tablas (es decir, si quedan barcos) o si intentos es mayor a 0
# en el caso de que alguna NO se cumpla, se termina el bucle
while quedan_barcos(tablero_propio) and quedan_barcos(tablero_maquina) and intentos > 0:
    
    resultado = "Tocado" # Este bloque es el mío, por defecto resultado será Tocado ya que si acierto, continúo yo. 
    while resultado == "Tocado" and quedan_barcos(tablero_maquina): # mientras resultado sea Tocado y queden barcos, sigo yo. Si no quedan barcos, se rompen los dos bucles while y gano
        
        while True: #agrego otro bucle while True con un try - except para que no se pueda poner ninguna letra, si no se elije entero no se sale del bucle
            
            try:
                time.sleep(1)
                print(f"Tienes {intentos} intentos")
                fila = int(input("Introduce la fila del 0 al 9 para disparar: "))          #elijo fila con un input entero
                columna = int(input("Introduce la columna del 0 al 9 para disparar: "))    # elijo columna con input entero
                if 0 <= fila <= 9 and 0 <= columna <= 9:
                    break
                else:
                    time.sleep(1)
                    print("Número fuera de rango, elije de nuevo por favor")
            except ValueError:
                time.sleep(1)
                print("Has entrado una letra. Elige un número por favor.")

        resultado = disparar((fila, columna), tablero_maquina) #llamo a disparar con argumento fila y columna (comprueba en tablero rival) y lo asigno a variable resultado
        time.sleep(1)
        print("Resultado:", resultado)
        if resultado == "Agua": # si resultado es agua, resto un intento y quiebro el bucle de mis intentos, continua la máquina
            intentos -= 1
            break

    # Turno de la máquina
    resultado_maquina = "Tocado" #este bloque es el de la maquina, mientras su resultado sea Tocado, sigue jugando. Si es agua, se rompen los bucles while identados y se reinicia el bucle while grande
    while resultado_maquina == "Tocado" and quedan_barcos(tablero_propio):
        fila_maquina = random.randint(0, 9) 
        columna_maquina = random.randint(0, 9) #filas y columnas se elijen con random, no indiqué la cantidad de intentos para la máquina
        resultado_maquina = disparar((fila_maquina, columna_maquina), tablero_propio) # se comprueba de la misma manera que en mi bloque
        time.sleep(1)
        print(f"La máquina disparó a ({fila_maquina}, {columna_maquina}): {resultado_maquina}")
        time.sleep(1)
        print(tablero_propio) #imprimo mi tablero para ver cómo va el juego, no  imprimo el suyo
        if resultado_maquina == "Agua":
            break #al brekearse este bloque, se reinicia el bloque grande que comprueba si hay barcos y si intentos es mayor a 0. Si es True, es mi turno, con un intento menos.

else: #si una de las condiciones es False, se termina naturalmente el bucle while y utilizo else para imprimir segun qué condición sea False
    if not quedan_barcos(tablero_propio):
        print("Perdiste: hundieron todos tus barcos.")
    elif not quedan_barcos(tablero_maquina):
        print("Ganaste: hundiste todos los barcos.")
    elif intentos <= 0: #en principio se imprimirá esto ya que sería poco probable ganar con 10 intentos
        print("Se acabaron tus intentos y tus compañeros deben exponer.")

#me quedó pendiente: avisar "has hundido un barco" si lograra hundir uno o si me hunden uno a mí

