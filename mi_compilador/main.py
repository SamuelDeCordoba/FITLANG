import sys
from lexer import tokenizar
from tokens import ErrorLexico, ErrorLiteral

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py ejemplo.txt")
        sys.exit(1)

    ruta = sys.argv[1]
    texto = open(ruta, encoding="utf-8").read()

    try:
        tokens = tokenizar(texto)
    except (ErrorLexico, ErrorLiteral) as e:
        print(e)
        sys.exit(1)

    print(f"{'LINEA':<6}{'COL':<5}{'TIPO':<15}TEXTO")
    for tipo, texto_tok, linea, columna in tokens:
        print(f"{linea:<6}{columna:<5}{tipo:<15}{texto_tok}")