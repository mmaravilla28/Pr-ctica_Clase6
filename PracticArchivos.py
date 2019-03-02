import string
import random

#función para escribir en el archivo
def escribir():
    letras = "abcdefghijklmnñopqrstuvwyz"
    numeros = "0123456789"
    nombre = ''
    apellido = ''
    telefono = ''

    #se genera el nombre aleatoriamente
    for i in range(10):
        nombre += random.choice(letras)

    #se genera el apellido aleatoriamente
    for J in range(10):
        apellido += random.choice(letras)

    #se crea el teléfono aleatoriamente
    for k in range(10):
        telefono += random.choice(numeros)

    #se crea el archivo y se escriben las líneas
    with open('datos.txt', 'a') as f:
            f.writelines([nombre,' ', apellido,' ', telefono, '\n'])

#se llama a la función que escribe en el archivo las 10 líneas
for l in range(10):
    escribir()

pass