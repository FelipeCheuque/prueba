import os
import json


matriz = [
    ["BULLDOG","TOBY",26.3]
]
menu = '''
1. registrar mascota
2. Mostrar lista
3. Buscar por especie
4. remover por nombre
5. Exportar listado general a TXT
6. Exportar datos a CSV
7. Exportar datos a JSON
0. Salir
'''

def exportarTXT(): # opcion 6
    with open('archivo.txt', 'w') as archivo:
	    archivo.write(matriz)
def exportarCSV(): # opcion 7
    import csv # permiso w es escritura
    with open('nuevo_archivo.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(['especie', 'nombre', 'peso'])

def exportarJSON(): # opcion 8
    with open('archivo.json', 'w') as archivo:
	    json.dump(matriz, archivo)


def buscarmascota():
    fila = matriz(input("indique la especie de la mascota : "))
    if fila == -1:
        print("no encontrado")
    else:
        print(f"entrado en fila: {fila}")
        print(f"su nombre: {matriz[fila][1]}")
        print(f"su peso: {matriz[fila][2]}")

    try: 
        for row in range(len(matriz)):
            if buscarmascota == matriz[row][0]:
                return row # si lo encuetra, se detiene y retorna la ubic
        return -1 # si llega a esta linea, no lo encontró, retorn -1
    except:
        input("excepcion al buscar por nombre")

def agregar():
    while True:
        try:
            os.system("cls")
            print("REGISTRANDO DATOS")
            especie = input("ESPECIE DE ANIMAL: ")
            encontrado = buscarmascota(especie)
            if encontrado == -1:
                input(f"{especie} no ha sido encontrado...")
                nom = input("nombre: ")
                especie = int(input("especie: "))
                matriz.append([especie,nom]) # creamos la lista [] y agregamos
                input("REGISTRO AGREGADO CON EXITO!")
                break # sale y regresa al main()
            else:
                print("rut ingresado previamente")
                input(f"los datos: {matriz[encontrado]}")
                break
        except:
            input("excepcion al ingresar")

def buscar():
    try:
        os.system("cls")
        print("BÚSQUEDA AVANZADA POR NOMBRE")
        row = buscarmascota(input("nombre a buscar: "))
        if row > -1:
                print(f"nombre: {matriz[row][1]}")
                print(f"especie: {matriz[row][2]}")
                input("\nEnter para continuar")
        else:
            input("no ha sido encontrado...")
    except:
        input("Excepcion al buscar")

def mostrar():
    try:
        os.system("cls")
        print("          LISTADO GENERAL")
        print("-----------------------------------------------")
        print("N°      ESPECIE        NOMBRE           PESO ")
        print("-----------------------------------------------")
        # recorrer y mostrar la informac de las filas y columnas
        for row in range(len(matriz)):
            print(f"{row+1:3d} ", end='') # numero desde 1 con ancho de 3
            print(f"{matriz[row][0]:12s}",end='') # rut, col 0, ancho de 12, String
            print(f"{matriz[row][1]:20s}",end='')    # nombre, col 1, ancho de 20s
            print(f"{matriz[row][2]:8d}",end='')    # sueldo, col 2, ancho de 8d
            print() # salto a la linea siguiente
        print("##############  FIN LISTADO   ###############")
        print(f"cantidad total de filas    = {len(matriz)}")
        print(f"cantidad de total columnas = {len(matriz[0])}")
        input("\nEnter para continuar...")
    except:
        input("excepcion al mostrar")

def remover():
    try:
        os.system("cls")
        # pedir RUT A remover
        fila = buscarmascota(input("mascota a remover: "))
        # verifica que los rangos sean desde 1 hasta len(matriz)
        if fila >= 0:
            # remueve utilizando .pop(fila), NO utilices .remove()
            mascota = matriz.pop(fila)
            input(f"{mascota} HA SIDO REMOVIDA CON EXITO")
        else:
            input("rut no encontrado...")
    except:
        input("excepcion al remover")

while True:
    try:
        os.system("cls")
        opc = int(input(menu))
        if opc == 0:
            break
        elif opc == 1:
            agregar()
        elif opc == 2:
            mostrar()
        elif opc == 3:
            buscar()
        elif opc == 4:
            remover()
        else:
            input("opcion incorrecta")
    except:
        input("excepcion de menu")

input("\nTerminando")