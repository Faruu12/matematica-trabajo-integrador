def obtener_conjunto_dni(dni):
    # convierte el DNI en una cadena y luego lo transforma en un conjunto de caracteres y elimina repetidos
    return set(str(dni))

def ingresar_dnis():
    cantidad = int(input("Ingrese la cantidad de integrantes: "))
    # crea una lista con los dni de cada integrante
    dnis = [input(f"Ingrese el DNI del integrante {i+1}: ") for i in range(cantidad)]
    conjuntos = [obtener_conjunto_dni(dni) for dni in dnis]
    return conjuntos

def operaciones_conjuntos(conjuntos):
    # calcula la unión de todos los conjuntos
    union = set.union(*conjuntos)
    
    # calcula la intersección de todos los conjuntos
    interseccion = set.intersection(*conjuntos)
    
    # calcula la diferencia entre pares consecutivos A - B
    diferencia_ab = [conjuntos[i] - conjuntos[i+1] for i in range(len(conjuntos)-1)]
    
    # calcula la diferencia entre pares consecutivos B - A
    diferencia_ba = [conjuntos[i+1] - conjuntos[i] for i in range(len(conjuntos)-1)]
    
    # calcula la diferencia simétrica entre todos los conjuntos A-B
    diferencia_simetrica = set.symmetric_difference(*conjuntos)

    # muestra el resultado de cada operación
    print(f"Unión de los conjuntos: {sorted(union)}")
    print(f"Intersección de los conjuntos: {sorted(interseccion)}")
    print(f"Diferencias A - B entre pares: {[sorted(dif) for dif in diferencia_ab]}")
    print(f"Diferencias B - A entre pares: {[sorted(dif) for dif in diferencia_ba]}")
    print(f"Diferencia simétrica A-B: {sorted(diferencia_simetrica)}")

def evaluar_condiciones(conjuntos):
    # si los conjuntos tienen al menos 5 digitos, se muestra mensaje
    if all(len(conjunto) > 5 for conjunto in conjuntos):
        print("Alta diversidad numérica")
    
    # si existe algún dígito que se encuentre en la intersección de todos los conjuntos se muestra mensaje
    if any(digito in conjunto for conjunto in conjuntos for digito in set.intersection(*conjuntos)):
        print("Dígito común encontrado")
    

# parte 2: operaciones con años de nacimiento

def ingresar_anos_nacimiento():
    cantidad = int(input("Ingrese la cantidad de integrantes: "))
    # crea una lista con los años de nacimiento ingresados
    anos = [int(input(f"Ingrese el año de nacimiento del integrante {i+1}: ")) for i in range(cantidad)]
    return anos

def analizar_anos(anos):
    # cuenta la cantidad de años pares
    pares = sum(1 for ano in anos if ano % 2 == 0)
    # calcula los años impares
    impares = len(anos) - pares

    print(f"Cantidad de años pares: {pares}")
    print(f"Cantidad de años impares: {impares}")

    # si todos los años ingresados son mayores a 2000, se muestra mensaje
    if all(ano > 2000 for ano in anos):
        print("Grupo Z")

    # si alguno de los años corresponde a un año bisiesto, se muestra un mensaje
    if any(es_bisiesto(ano) for ano in anos):
        print("Tenemos un año especial")

def es_bisiesto(ano):
    # determina si un año es bisiesto
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

from itertools import product  # importa la función product para calcular productos cartesianos

def calcular_producto_cartesiano(anos):
    # la edad se obtiene restando el año de nacimiento del año actual
    edades = [2025 - ano for ano in anos]
    # calcula el producto cartesiano entre la lista de años y la lista de edades, generando una lista de tuplas
    producto = list(product(anos, edades))
    # muestra el resultado del producto cartesiano
    print("Producto cartesiano entre años y edades:", producto)

def main():     
    # procesamiento de DNIs
    conjuntos_dni = ingresar_dnis()
    operaciones_conjuntos(conjuntos_dni)
    evaluar_condiciones(conjuntos_dni)

    # procesamiento de años de nacimiento
    anos_nacimiento = ingresar_anos_nacimiento()
    analizar_anos(anos_nacimiento)
    calcular_producto_cartesiano(anos_nacimiento)

# llamada directa a main
main()
