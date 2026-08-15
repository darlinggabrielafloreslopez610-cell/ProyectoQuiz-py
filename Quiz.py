# Muestra una línea de 50 guiones bajos
print("_" * 50)
print("---QUIZ INTERACTIVO DE PROGRAMACIÓN---")# Muestra el título principal del programa
print("_" * 50) #Muestra otra línea para separar el título
print()  # Deja un espacio en blanc0
print("¡Bienvenido al Quiz!")# Muestra  un mensaje de Bienvenida
print()

preguntas = [ #Lista que almacena todas las preguntas del Quiz
    {
        "pregunta": "¿Qué función permite mostrar información en Python?", # Cada Diccionario almacena los datos de una pregunta
        "opciones": [ # Lista que almacena las opciones de la respuesta
         "A. Input()",
         "B. Print()",
         "C. Len()",
         "D. Type()",
        ],
        "respuesta": "B",
        "categoria": "Python"
    },

    {
        "pregunta": "¿Qué estructura se utiliza para repetir un bloque de código un número determinado de veces?",
        "opciones": [
         "A. Condicional()",
         "B. Ciclo for()",
         "C. Diccionario()",
         "D. Variable()",
        ],
        "respuesta": "B",
        "categoria": "Ciclos"
    },

    {
        "pregunta": "¿Cuál es la forma correcta de definir una lista en Python?",
        "opciones": [
         "A. Lista = {1,2,3}",
         "B. Lista = (1,2,3)",
         "C. Lista = [1,2,3]",
         "D. Lista = <1,2,3>]",
        ],
        "respuesta": "C",
        "categoria": "Listas"
    },
    
    {
        "pregunta": "¿Qué función utilizas en python para capturar un dato ingresado por el usuario a través de la consola?",
         "opciones": [
         "A. Print",
         "B. type",
         "C. Input",
         "D. int ",
        ],
        "respuesta": "C",
        "categoria": "Variables"
    },
    
    {
        "pregunta": "¿Si necesitas almacenar el nombre de un estudiante para el reporte, ¿qué tipo de dato es el más adecuado?",
         "opciones": [
         "A. int",
         "B. float ",
         "C. bool ",
         "D. string",
        ],
        "respuesta": "D",
        "categoria": "Variables"       
    },
    
] 
resultados =[] #Lista que almacena los resultados obtenidos por el usaurio

def iniciar_quiz(): #Función que permite Iniciar y Responder el Quiz
       print()
       print("-" * 50)
       print(" CUESTIONARIO")
       print("-" * 50)
       print()

       nombre = input("Ingrese su nombre: ") # Solicita al usuario que ingrese su nombre

       print()
       print("¡Bienvenido (a) al cuestionario,", nombre + "!")
       print()
       Puntuación = 0 # Inicia la puntuación del usuario en 0
       
       for numero , pregunta in enumerate (preguntas , start=1): # Recorre todas las preguntas del Quiz una por una
           print("-" * 50)
           print("Pregunta", numero, "de", len(preguntas))
           print("-" * 50)
           print (pregunta["pregunta"])
           print()
           
           for opcion in pregunta["opciones"]: # Recorre las opciones de la pregunta actual
                print(opcion)
           respuesta_usuario = input("Elija una opción (A, B, C, D): ").upper() # Se solicita al usuario que seleccione una respuesta
           if respuesta_usuario == pregunta["respuesta"]: # Comprueba si la respuesta del usuario es correcta
                print("¡Correcto!\n")
                Puntuación += 1 # Aumenta un punto por cada respuesta correcta
           else: # Se ejecuta cuando la respuesta del usuario es incorrecta
                print("Incorrecto. La respuesta era:", pregunta["respuesta"], "\n")   
                print()
                print()
       print("QUIZ Finalizado") # Mensaje
       resultados.append({ # Guarda el resultado del usuario  en la lista de resultados
       "nombre": nombre,
       "puntuacion": Puntuación,
       "total": len(preguntas)
})

def administrar_preguntas(): #Función que permite Agregar,Modificar,Eliminar y Consultar Preguntas
    while True: #   Repite el menú hasta que el usuario desee regresar
        print()
        print()
        print("-" * 50)
        print(" ADMINISTRAR PREGUNTAS")
        print("-" * 50)
        print("1. Ver preguntas")
        print("2. Agregar pregunta")
        print("3. Modificar pregunta")
        print("4. Eliminar pregunta")
        print("5. Regresar al menú principal")

        opcion = input("Seleccione una opción: ")

        # Ver preguntas
        if opcion == "1":
            print()
            print("-" * 50)
            print(" LISTA DE PREGUNTAS")
            print("-" * 50)

            for numero, pregunta in enumerate(preguntas, start=1): # Recorre todas las Preguntas Para mostrarlas en la opción administrar preguntas
                print()
                print("Pregunta", numero, ":", pregunta["pregunta"])

                for opcion_respuesta in pregunta["opciones"]: # Recorre las Opciones de Cada pregunta para mostrarlas
                    print(opcion_respuesta)

                print("Respuesta correcta:", pregunta["respuesta"])
                print("Categoría:", pregunta["categoria"])

        
        elif opcion == "2": # Agregar pregunta
            print()
            print("-" * 50)
            print(" AGREGAR PREGUNTA")
            print("-" * 50)

            nueva_pregunta = input("Ingrese la pregunta: ")

            opciones = []
            opciones.append("A. " + input("Ingrese la opción A: "))
            opciones.append("B. " + input("Ingrese la opción B: "))
            opciones.append("C. " + input("Ingrese la opción C: "))
            opciones.append("D. " + input("Ingrese la opción D: "))

            respuesta = input("Ingrese la respuesta correcta (A, B, C o D): ").upper()
            categoria = input("Ingrese la categoría: ")

            preguntas.append({ # Agrega la nueva pregunta a la lista de preguntas
                "pregunta": nueva_pregunta,
                "opciones": opciones,
                "respuesta": respuesta,
                "categoria": categoria
            })

            print()
            print("¡Pregunta agregada correctamente!")

       
        elif opcion == "3": # Modificar pregunta
            print()
            print("-" * 50)
            print(" MODIFICAR PREGUNTA")
            print("-" * 50)

            for numero, pregunta in enumerate(preguntas, start=1): # Este For recorre todas las preguntas de la lista y las muestra una por una 
                print(numero, ".", pregunta["pregunta"])

            numero = int(input("Ingrese el número de la pregunta que desea modificar: "))

            if 1 <= numero <= len(preguntas): # Comprueba que el número de la pregunta sea válido
                pregunta = preguntas[numero - 1]

                pregunta["pregunta"] = input("Ingrese la nueva pregunta: ")

                pregunta["opciones"] = [
                    "A. " + input("Ingrese la nueva opción A: "),
                    "B. " + input("Ingrese la nueva opción B: "),
                    "C. " + input("Ingrese la nueva opción C: "),
                    "D. " + input("Ingrese la nueva opción D: ")
                ]

                pregunta["respuesta"] = input(
                    "Ingrese la nueva respuesta correcta (A, B, C o D): "
                ).upper()

                pregunta["categoria"] = input("Ingrese la nueva categoría: ")

                print()
                print("¡Pregunta modificada correctamente!")

            else:
                print("Número de pregunta no válido.")

        
        elif opcion == "4": # Eliminar pregunta
            print()
            print("-" * 50)
            print(" ELIMINAR PREGUNTA")
            print("-" * 50)

            for numero, pregunta in enumerate(preguntas, start=1):
                print(numero, ".", pregunta["pregunta"])

            numero = int(input("Ingrese el número de la pregunta que desea eliminar: "))

            if 1 <= numero <= len(preguntas):
                preguntas.pop(numero - 1) #Elimina la pregunta Seleccionada de la lista
                print()
                print("¡Pregunta eliminada correctamente!")
            else:
                print("Número de pregunta no válido.")

        
        elif opcion == "5":  # Regresar al Menú principal
            break  # Hace que salgas del menú de administración al menú principal

        else:
            print("Opción no válida. Intente nuevamente.")
            
def ver_resultados(): # Función que permite consultar los resultados obtenidos
    print()
    print("-" * 50)
    print(" RESULTADOS")
    print("-" * 50)

    if len(resultados) == 0: # Comprueba si hay resultados registrados
        print("No hay resultados registrados.")
    else:
        for numero, resultado in enumerate(resultados, start=1): # Recorre todos los resultados almacenados
            print()
            print("Resultado", numero)
            print("Nombre:", resultado["nombre"])
            print("Puntuación:", resultado["puntuacion"], "de", resultado["total"])

    print()
    input("Presione Enter para regresar al menú principal...") 

while True:
        print("----MENÚ PRINCIPAL ----")
        print("1. Iniciar Quiz")
        print("2. Administrar Preguntas")
        print("3. Ver Resultados")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion =="1": # Permite Iniciar el Quiz
         iniciar_quiz()
         print("Ha seleccionado Iniciar Quiz")
         print("\n")
        elif opcion == "2": # Permite administar las Preguntas
         administrar_preguntas()

        elif opcion == "3": # Permite consultar los resultados
          print("Ha seleccionado Ver Resultados")
          print("\n")
          ver_resultados()

        elif opcion == "4": # Permite Salir del programa
          print("¡Gracias por utilizar el Quiz!")
          break # Detiene el ciclo principal y Finaliza el programa

        else:
         print("Opción no válida. Intente nuevamente.")
         print("\n")