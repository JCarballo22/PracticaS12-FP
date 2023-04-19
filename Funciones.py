#funciones en Python

def Mensaje():
    print("Hola Grupo fundamentos de programación")

Mensaje()

def Nombre(nombre):
    print("Hola",nombre)

Nombre("Ana Yancy")

entraNombre = input("Ingresa tu nombre: ")
Nombre(entraNombre)
Nombre(input("Digita otro nombre"))

def Multiplicar(numero,multi):
    print(f"{numero}*{multi} = {numero*multi}")

print("Comienzo del programa")
Multiplicar(6,4)
print("Otra forma")
Multiplicar(int(input("Ingrese un numero: ")),int(input("Ingrese un numero a multiplicar: ")))
print("Fin")

def suma(a,b):
    resultado = a + b
    return resultado

print("El resultado de la suma es: ",suma(8,9))

resulSuma = suma(6,4)
print("El resultado de la suma es: ",resulSuma)

def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ","")
    print(cadena)
    return cadena == cadena[::-1]

texto = "Anita lava la tina"
if es_palindromo(texto):
    print("El texto es un políndromo")
else:
    print("El texto no es un políndromo")

def validaCorreo():
    #Ejemplo validación de correo
    email = False

    for i in "mauricio@gmail.com":
        if i == "@":
            email=True

    if email ==True:
        print("Email es correcto")
    else:
        print("Email es incorrecto")


def validaCorreo2():
    valido = False
    email = input("Digite su correo: ")
    for i in range(len(email)):
        if email[i] =="@":
            valido = True
    if valido == True:
        print("Email es correcto")
    else:
        print("Email es incorrecto")

validaCorreo2()
print("Fin")