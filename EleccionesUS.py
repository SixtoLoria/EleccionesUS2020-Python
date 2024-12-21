# En esta prectica vamos a trabajar con otro archivo de datos CSV.
# En un archivo CSV posee sus datos separados por comas.
# Se lee la informacion contenida en el archivo US2020_ElectionsResults.CSV
# Usuario: Sixto Loria Villagra
# Fecha: 13/11/2020
# Version: 02

# Importando librerias.
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

# BORRAR PANTALLA.f
Borrar_pantalla = lambda: os.system("cls")
# FUNCIONES

def leer_numero(Mensaje, Tipo):
    """Esta funcion es para recibir numeros del usuario y validarlos"""
    while True:
        # Solicitando un entero del teclado
        Numero =  input(Mensaje)
        # validacion
        try:
            if Tipo == "Entero":
                #Transformando numero a entero
                Numero = int(Numero)
                # Salida del cliclo while
                return Numero
            elif Tipo == "Flotante":
                # Convertir numero a flotante
                Numero = float(Numero)
                return Numero
            else:
                # El usuario no inserto un numero
                print("ERROR, dato insertado no es un numero")
        except ValueError:
            print("ERROR, dato insertado no es un numero")
    # Retornando el numero validado al programa
    return Numero


def validar_opcion(Mensaje, Opciones):
    """Solicitarle al usuario que seleccione una opicion valida"""
    # Ciclo de validacion
    while True:
        # solicitar el usuario que seleccione una de las opciones
        Opcion = leer_numero(Mensaje, "Entero")
        # Necesitamos saber cuantas opciones hay en la lista
        Num_Op = len(Opciones)
        # Validar la opcion
        for Indice in range(Num_Op):
            # Verificar si opcion esta en la lista
            if Opcion == Opciones[Indice]:
                # Opcion valida
                return Opcion
        # si Salimos del ciclo for sin que hubiera coincidencia
        print("ERROR, el dato insertado no esta entre las opciones")


def validar_decision(Mensaje):
    """Esta funcion valida si el usuario desea aceptar una opcion seleccionada"""
    # Creando condicion de validacion
    Condicion = True
    # Ciclo wihle de repetcion
    while Condicion:
        # Preguntar al usuario si desea repetir la opcion
        Letra = input(Mensaje)
        # Validar la Opcion seleccionada
        if Letra == "S" or Letra == "s":
            # Usuario desea repetir
            return True
        elif Letra == "N" or Letra == "n":
            # Usuario quiere salir
            return False
        else:
            # opcion seleccionada es invalida
            print("ERROR:, La opcion seleccionada es invalida")

# PROGRAMA PRINCIPAL-------------------------------------------------------------------------------
# Lectura de la infromacion contenida en el archivo: Libra vs Dolar.csv
# Creando lista para alojar la informacion de archivo
Resultados = []
# Estructura de lectura del archivo
with open("US2020_ElectionsResults.csv", mode="r") as Archivo:
    # Creando un objeto de lectura para el archivo CSV
    Csv_Archivo = csv.reader(Archivo)
    # Leyendo las filas del archivo y pasando la informacion a la lista
    for Registro in Csv_Archivo:
        # Cargando cada fila de infromacion en la lista.
        Resultados += [Registro]
# Mensaje de final de lectura
print("El Archivo se leyo correctamente")

# Ciclo de repeticion
Repetir = True
# Ciclo principal
while Repetir:
    # Borrando pantalla
    Borrar_pantalla()
    # Mostrando el menu principal
    print("***************************************************************************************")
    print("**                                                                                   **")
    print("**       RESULTADOS DE LAS ELECCIONES PRESIDENCIALES EN EE.UU - NOVIEMBRE 2020       **")
    print("**                                                                                   **")
    print("***************************************************************************************\n")

    print("MENU PRINCIPAL: ")
    print()
    print("1) Listado de los resultados en todos los estados")
    print("2) Graficacion de resultados en un estado en particular")
    print("3) Grafico de resultados a nivel Nacional.")
    print("4) Salir del programa")
    # Solicitar al usuario que seleccione una opcion
    Opcion = validar_opcion("Seleccione una opcion: ", (1, 2, 3, 4))
    # Analizar la opcion sellecionada
    if Opcion == 1:
        # Modulo de la tabla
        Borrar_pantalla()
        print("***************************************************************************************")
        print("**                MODULO DE RESULTADOS GENERALES PARA TODOS LOS ESTADOS              **")
        print("***************************************************************************************\n")
        print("Tabla de Resultados Generales por estado")
        # Presentando los datos en la forma de una tabla.
        # Creando una lista vacia
        Resultados_Extra = []
        # Creando una nueva tabla
        Tabla = PrettyTable(["Estado", "Vostos Biden", "Votos Trump", "Total", "Ganador", "Mesas procesadas"])
        # Calculando total de estados
        N_Estados = len(Resultados) - 1
        # Ciclo for para agregar filas a la tabla
        for estado in range(1, N_Estados + 1):
            # Crear una fila vacia
            Fila = []
            # Tomando los datos de la lista original
            Datos = Resultados[estado]
            # Agregando nombre de estado a la fila
            Fila += [Datos[0]]
            # Agregando votos de Biden
            Fila += [Datos[1]]
            # Agregando votos de trump
            Fila += [Datos[2]]
            # Agregando Total de votos del estado
            Fila += [int(Datos[1]) + int(Datos[2])]
            # Generando ganador del estado
            if int(Datos[1]) > int(Datos[2]):
                # El ganador es Biden
                Fila += ["Biden"]
            else:
                # El ganador es Trump
                Fila += ["Trump"]
            # Agregando el % de mesas procesadas
            Fila += [Datos[3]]
            # Agregando la nueva fila a la tabla
            Tabla.add_row(Fila)
            # Agregando la nueva fila a la nueva lista
            Resultados_Extra += [Fila]
        # Mostrando la tabla en pantalla
        print(Tabla)
        # Mostrando un mensaje
        print("Fuente: NBC News Online")
        print()
        # Creacion de nuevo archivo CSV Con los datos de la tabla
        Condicion03 = validar_decision("Desea guardar los datos de la tabla (S/N)? ")
        # Verificando opcion
        if Condicion03:
            # Salvando informacion de la tabla en archivo
            with open("US2020_EleResultsExtra.csv", mode="w", newline="") as Archivo:
                # Crear Objeto de escritura para el archivo
                Csv_Archivo = csv.writer(Archivo, delimiter=",")
                # Calculando Numero de filas a escribir en archivo
                N_Filas = len(Resultados_Extra)
                # Escribiendo primera fila del archivo
                Csv_Archivo.writerow(["Estado", "Vostos Biden", "Votos Trump", "Total", "Ganador", "Mesas procesadas"])
                # Ciclo for de escritura
                for fila in range(N_Filas):
                    # Colocando fila de informacion en el archivo
                    Csv_Archivo.writerow(Resultados_Extra[fila])
                # Mensaje de confirmacion para el usuario
                print("Informacion Guardada correctamente")
        input("Pressione ENTER Para volver al menu principal")
    elif Opcion == 2:
        # Calculando total de estados
        N_Estados = len(Resultados) - 1
        # Condiccion de repeticion del modulo 2
        Condicion02 = True
        # Ciclo de repeticion del modulo 2
        while Condicion02:
            Borrar_pantalla()
            print("***************************************************************************************")
            print("**             MODUL0 GRAFICO DE RESULTADOS PARA UN ESTADO EN PARTICULAR             **")
            print("***************************************************************************************\n")
            # Modulo de resultados en graficacion para un estado
            # Mostranddo grafico de pastel para un estado en particular
            # Solicitando al usuario que seleccione un estado
            Estado_Referencia = input("Inserte el Nombre del estado que desea graficar: ")
            # Generando contador para verificar si el archivo buscando existe
            Contador = 0
            # Creando una condicion
            Encontrado = False
            # Buscando estado seleccionado en la lista
            for estado in range(1, N_Estados + 1):
                # Preguntar por el nombre del estado
                if Resultados[estado][0] == Estado_Referencia:
                    # Generaando el grafico
                    print("Estado solicitado esta en la lista")
                    # Extraer la informacion de estado seleccionado
                    Etiquetas = np.array(["Joe Biden", "Donald Trump"])
                    Datos = np.array([int(Resultados[estado][1]), int(Resultados[estado][2])])
                    # Creando titulo para el grafico
                    Titulo = "Resultados Provicionales en el estado de " + Estado_Referencia
                    # Generando grafico de Pastel
                    plt.pie(Datos, labels=Etiquetas, colors=["b", "r"], autopct="%.2f%%")
                    plt.title(Titulo)
                    plt.show()
                    # Cambiando condicion
                    Encontrado = True
                    # Saliendo de ciclo For
                    break
            # Revisando si el estado fue encontrado
            if not Encontrado:
                # Mostrando mensaje de Error
                print("ERROR: El estado solicitado no esta en la lista")
            # Validando repeticion de la opcion
            Condicion02 = validar_decision("Desea Buscar y graficar otro estado(S/N)? ")

    elif Opcion == 3:
        # Modulo de resultados a nivel nacional
        Borrar_pantalla()
        print("***************************************************************************************")
        print("**                             RESULTADOS A NIVEL NACIOANL                           **")
        print("***************************************************************************************\n")
        # Convirtiendo lista original en arreglo
        Arreglo_Res = np.array(Resultados)
        # Calculando el numero de filas del arreglo original
        N_Arreglo = len(Arreglo_Res)

        # Quitando los encabezados de la primera fila
        Arreglo_Res = Arreglo_Res[1:N_Arreglo, :]
        # Extraer los votos a cada candidato en todos los estados
        V_Biden = Arreglo_Res[:, 1]
        V_Trump = Arreglo_Res[:, 2]
        # Convirtiendo vectores de caracteres a vectores de numeros
        V_Biden = V_Biden.astype(np.int)
        V_Trump = V_Trump.astype(np.int)
        # Generar la sumatoria de todos esos votos
        Total_Biden = np.sum(V_Biden)
        Total_Trump = np.sum(V_Trump)
        # Preparando Datos del grafico de pastel
        Etiquetas = np.array(["Joe Biden", "Donald Trump"])
        Datos = np.array([Total_Biden,Total_Trump])
        # Creando un titulo para el grafico
        Titulo = "RESULTADOS DE LAS ELECCIONES A NIVEL NACIONAL"
        # Generando grafico de Pastel
        plt.pie(Datos, labels=Etiquetas, colors=["b", "r"], autopct="%.2f%%")
        plt.title(Titulo)
        plt.show()
        # Mensaje para volver al menu principal
        input("Presione ENTER Para volver lal Menu Princial")
    else:
        # Salida de la aplicacion
        Repetir = False

# Mensaje de salida
Borrar_pantalla()
print("***************************************************************************************")
print("**                                                                                   **")
print("**       RESULTADOS DE LAS ELECCIONES PRESIDENCIALES EN EE.UU - NOVIEMBRE 2020       **")
print("**                                                                                   **")
print("***************************************************************************************\n")
print("Usted esta saliendo de la aplicacion...")
input("Presione ENTER para salir")