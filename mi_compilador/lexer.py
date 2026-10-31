# lexer.py
from tokens import ErrorLexico, ErrorLiteral

PALABRAS_RESERVADAS = {"rutina", "ejercicio", "series", "repeticiones", "peso",
                       "descanso", "objetivo", "activo", "si", "sino", "y", "o"}
SIMBOLOS = {"=", ";", "{", "}", "(", ")", ",", "."}
OPERADORES = {"+", "-", "*", "<", ">"}
DIGITOS = "0123456789"
BOOLEANOS = {"verdadero", "falso"}


def tokenizar(texto):
    tokens = []
    i = 0
    linea = 1
    columna = 1

    while i < len(texto):
        c = texto[i]

        if c == "\n":
            i += 1
            linea += 1
            columna = 1

        elif c in " \t\r":
            i += 1
            columna += 1

        elif c == "#":
            while i < len(texto) and texto[i] != "\n":
                i += 1
                columna += 1

        elif c in DIGITOS:
            inicio = i
            col_inicio = columna

            while i < len(texto) and texto[i] in DIGITOS:
                i += 1
                columna += 1

            if i < len(texto) and texto[i] == ".":
                if i + 1 < len(texto) and texto[i + 1] in DIGITOS:
                    i += 1
                    columna += 1
                    while i < len(texto) and texto[i] in DIGITOS:
                        i += 1
                        columna += 1
                    if i < len(texto) and texto[i] == ".":
                        raise ErrorLiteral(
                            "decimal mal formado", linea, col_inicio)
                else:
                    raise ErrorLiteral(
                        "decimal mal formado", linea, col_inicio)

            numero = texto[inicio:i]
            tokens.append(("NUMERO", numero, linea, col_inicio))

        elif c == '"':
            inicio = i
            col_inicio = columna
            i += 1
            columna += 1
            while i < len(texto) and texto[i] != '"' and texto[i] != '\n':
                i += 1
                columna += 1
            if i >= len(texto) or texto[i] == '\n':
                raise ErrorLiteral("cadena sin cerrar", linea, col_inicio)

            i += 1
            columna += 1
            cadena = texto[inicio:i]
            tokens.append(("CADENA", cadena, linea, col_inicio))

        elif c.isalpha() or c == "_":
            inicio = i
            col_inicio = columna
            while i < len(texto) and (texto[i].isalnum() or texto[i] == "_"):
                i += 1
                columna += 1
            palabra = texto[inicio:i]

            if palabra.lower() in PALABRAS_RESERVADAS:
                tokens.append(("RESERVADA", palabra, linea, col_inicio))
            else:
                tokens.append(("IDENTIFICADOR", palabra, linea, col_inicio))

        elif texto.startswith(("==", "<=", ">="), i):
            tokens.append(("OPERADOR", texto[i:i + 2], linea, columna))
            i += 2
            columna += 2

        elif c in SIMBOLOS:
            tokens.append(("SIMBOLO", c, linea, columna))
            i += 1
            columna += 1

        elif c in OPERADORES:
            tokens.append(("OPERADOR", c, linea, columna))
            i += 1
            columna += 1

        else:
            raise ErrorLexico(c, linea, columna)

    return tokens