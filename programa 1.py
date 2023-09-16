def contar_letras_a(cadena):
    contador = 0
    for letra in cadena:
        if letra.lower() == 'a':
            contador += 1
    return contador
cadena_usuario = input("Ingresa una oración: ")
cantidad_a = contar_letras_a(cadena_usuario)
print(f"La cantidad de letras 'a' en la cadena es: {cantidad_a}")

