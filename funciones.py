lista=(int(input("Ingrese su apellido: ")))
def validador (lista, buscar):
    for i in range (len(lista)):  
        if (lista[i] == buscar ):
            return True
        break
    return False