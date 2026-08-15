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

