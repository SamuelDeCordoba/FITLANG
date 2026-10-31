class ErrorLexico(Exception):
    def __init__(self, caracter, linea, columna):
        self.caracter = caracter
        self.linea = linea
        self.columna = columna
        super().__init__(
            f"Error léxico: el carácter {caracter!r} no pertenece al lenguaje "
            f"(línea {linea}, columna {columna})"
        )


class ErrorLiteral(Exception):
    def __init__(self, mensaje, linea, columna):
        self.linea = linea
        self.columna = columna
        super().__init__(
            f"Error léxico: {mensaje} (línea {linea}, columna {columna})")