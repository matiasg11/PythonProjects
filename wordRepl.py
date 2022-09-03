string = "Hola, soy Matias y y estoy probando un reemplazador de palabras."

def reemplazar(string):

    palabra_saliente = input("¿Qué palabra hay que reemplazar? ")
    palabra_entrante = input("¿Qué palabra hay que ingresar? ")
    string = string.replace(palabra_saliente, palabra_entrante)
    print(string.replace(palabra_saliente, palabra_entrante))


reemplazar(string)