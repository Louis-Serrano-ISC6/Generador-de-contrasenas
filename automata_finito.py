automata = {
    "0": [("1", "e")],
    "1": [("2", "a"), ("3", "b"), ("4", "c"), ("5", "d")],
    "2": [("6", "b"), ("7", "c"), ("8", "d"), ("2", "f")],
    "3": [("6", "a"), ("9", "c"), ("10", "d"), ("3", "f")],
    "4": [("7", "a"), ("9", "b"), ("11", "d"), ("4", "f")],
    "5": [("7", "a"), ("9", "b"), ("11", "c"), ("5", "f")],
    "6": [("12", "c"), ("13", "d"), ("6", "f")],
    "7": [("12", "b"), ("14", "d"), ("7", "f")],
    "8": [("13", "b"), ("14", "c"), ("8", "f")],
    "9": [("12", "a"), ("15", "d"), ("9", "f")],
    "10": [("13", "a"), ("14", "c"), ("10", "f")],
    "11": [("14", "a"), ("15", "b"), ("11", "f")],
    "12": [("16", "d"), ("12", "f")],
    "13": [("16", "c"), ("13", "f")],
    "14": [("16", "b"), ("14", "f")],
    "15": [("16", "a"), ("15", "f")],
    "16": [("16", "e")],
}


def validar_minusculas(caracter: str) -> bool:
    return 'a' <= caracter <= 'z'


def validar_mayusculas(caracter: str) -> bool:
    return 'A' <= caracter <= 'Z'


def validar_digitos(caracter: str) -> bool:
    return '0' <= caracter <= '9'


def validar_caracteres_especiales(caracter: str) -> bool:
    return caracter in "@-*?"


def validar_mayusculas_minusculas(caracter: str) -> bool:
    return validar_minusculas(caracter) or validar_mayusculas(caracter)


def validar_todo(caracter: str) -> bool:
    return (validar_mayusculas_minusculas(caracter) or
            validar_digitos(caracter) or
            validar_caracteres_especiales(caracter))

def analizar_cadena(cadena: str) -> list:
    estado_actual = "0"
    pasos = []
    pasos.append(estado_actual + cadena + "\n")
    for i in range(len(cadena)):
        if i >= 15:
            break

        simbolo = cadena[0]
        transiciones = automata.get(estado_actual, [])
        encontrada = False

        for destino, tipo in transiciones:
            if diccionario_caracteres[tipo](simbolo):
                estado_actual = destino
                cadena = cadena[1:]
                pasos.append(f"{estado_actual}{cadena}\n")
                encontrada = True
                break

        if not encontrada:
            break

    if estado_actual in {"12", "13", "14", "15", "16"}:
        pasos.append(f"{estado_actual} ϵ F ∴ se acepta\n")
        return pasos

    else:
        pasos.append(f"{estado_actual} ∉ F ∴ se rechaza\n")
        return pasos






diccionario_caracteres = {
    "a": validar_minusculas,
    "b": validar_mayusculas,
    "c": validar_digitos,
    "d": validar_caracteres_especiales,
    "e": validar_mayusculas_minusculas,
    "f": validar_todo,
}

"""if __name__ == "__main__":
    cadena = input("Ingrese la cadena a validar: ")
    resultado = analizar_cadena(cadena)
    for paso in resultado:
        print(paso)"""