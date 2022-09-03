#Store q and a in a dictionary/object
#keep track of the score
#Print the questions and ask for the answers
#Check the answer
#Show final score

quiz = {
    "Pregunta 1":{
        "pregunta": "De qué color era el caballo blanco de San Martin?",
        "respuesta": "Blanco"
    },
    "Pregunta 2":{
        "pregunta": "Cual es la raiz cuadrada de 2?",
        "respuesta": "1,414213562"
    },
    "Pregunta 3":{
        "pregunta": "La capital de Bulgaria?",
        "respuesta": "Sofia"
    },
    "Pregunta 4":{
        "pregunta": "Nombre de mi tía?",
        "respuesta": "Eulalia"
    },
    "Pregunta 5":{
        "pregunta": "Campeón mundial del 34?",
        "respuesta": "Italia"
    },
}

puntaje = 0

for key, value in quiz.items():
    print(value["pregunta"])
    respuesta = input("Respuesta? ")
    if respuesta.lower() == value["respuesta"].lower():
        print("¡Correcto!")
        puntaje = puntaje + 1
        print("Tu puntaje: ", str(puntaje))
    else:
        print("Estás loc@, la respuesta es ", value["respuesta"])
        print("Tu puntaje: ", str(puntaje))

print("Puntaje final: ", puntaje, ". Es decir, un",str(puntaje*20),"%.")