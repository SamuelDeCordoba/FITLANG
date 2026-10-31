# pruebas.py
from lexer import tokenizar
from tokens import ErrorLexico, ErrorLiteral

casos = [

    ("peso = 72.5;",
     [("RESERVADA", "peso", 1, 1), ("SIMBOLO", "=", 1, 6), ("NUMERO", "72.5", 1, 8), ("SIMBOLO", ";", 1, 12)]),

    ("peso=a+5*2;",
     [("RESERVADA", "peso", 1, 1), ("SIMBOLO", "=", 1, 5), ("IDENTIFICADOR", "a", 1, 6), ("OPERADOR", "+", 1, 7),
      ("NUMERO", "5", 1, 8), ("OPERADOR", "*", 1, 9), ("NUMERO", "2", 1, 10), ("SIMBOLO", ";", 1, 11)]),

    ('rutina = "Pierna"; # fuerte\npeso = 40.5;',
     [("RESERVADA", "rutina", 1, 1), ("SIMBOLO", "=", 1, 8), ("CADENA", '"Pierna"', 1, 10), ("SIMBOLO", ";", 1, 18),
      ("RESERVADA", "peso", 2, 1), ("SIMBOLO", "=", 2, 6), ("NUMERO", "40.5", 2, 8), ("SIMBOLO", ";", 2, 12)]),

    ("peso = 80 @;", (1, 11)),

    ("peso = 3.4.5;", (1, 8)),

    ('peso = 80;\nrutina = "Brazo;', (2, 10)),

    ("(a+b)*2;",
     [("SIMBOLO", "(", 1, 1), ("IDENTIFICADOR", "a", 1, 2), ("OPERADOR", "+", 1, 3), ("IDENTIFICADOR", "b", 1, 4),
      ("SIMBOLO", ")", 1, 5), ("OPERADOR", "*", 1, 6), ("NUMERO", "2", 1, 7), ("SIMBOLO", ";", 1, 8)]),

    ("System.out",
     [("IDENTIFICADOR", "System", 1, 1), ("SIMBOLO", ".", 1, 7), ("IDENTIFICADOR", "out", 1, 8)]),

    ("x = 3.14;",
     [("IDENTIFICADOR", "x", 1, 1), ("SIMBOLO", "=", 1, 3), ("NUMERO", "3.14", 1, 5), ("SIMBOLO", ";", 1, 9)]),

        ("si siempre si_x",
     [("RESERVADA", "si", 1, 1), ("IDENTIFICADOR", "siempre", 1, 4), ("IDENTIFICADOR", "si_x", 1, 12)]),

    ("activo verdadero",
     [("RESERVADA", "activo", 1, 1), ("BOOLEANO", "verdadero", 1, 8)]),

    ("sino falso",
     [("RESERVADA", "sino", 1, 1), ("BOOLEANO", "falso", 1, 6)]),
]

print("--- EJECUCIÓN DE EVALUACIÓN PARCIAL 2 ---")
for entrada, esperado in casos:
    try:
        real = tokenizar(entrada)
    except (ErrorLexico, ErrorLiteral) as e:
        real = (e.linea, e.columna)

    coincide = "SI" if real == esperado else "NO"

    print(f"\nEntrada analizada:\n{repr(entrada)}")
    print(f"  Esperado a mano: {esperado}")
    print(f"  Resultado real:  {real}")
    print(f"  ¿Coinciden?:     {coincide}")