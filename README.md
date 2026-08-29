# FitLang

**FitLang** es un lenguaje de dominio específico (DSL) diseñado para describir rutinas de entrenamiento de forma simple, estructurada y legible. Permite crear rutinas, definir ejercicios, series, repeticiones, peso, descanso, objetivos, y tomar decisiones automáticas sobre el rendimiento del usuario.

## Grupo 9

- Samuel Córdoba Hernández
- Camilo Andrés Mora
- Fino Eduardo Fino
- Mariana Martínez

## Qué puede hacer FitLang

- Crear rutinas de entrenamiento.
- Agregar ejercicios a una rutina.
- Definir series, repeticiones, peso y descanso.
- Establecer un objetivo (fuerza, hipertrofia, resistencia).
- Saber si un ejercicio está activo.
- Evaluar el rendimiento del usuario.
- Decidir automáticamente si se debe **aumentar**, **disminuir** o **mantener** el peso.

## Tipos de datos del lenguaje

| Tipo      | Ejemplo               |
|-----------|------------------------|
| Texto     | `"Sentadilla"`         |
| Entero    | `4`, `12`, `90`        |
| Número    | `40`, `40.5`           |
| Booleano  | `verdadero`, `falso`   |

## Tabla de clasificación de variables

| Variable | Tipo Python | Ejemplo |
|---|---|---|
| `rutina` | `str` | `"Pierna"` |
| `ejercicio` | `str` | `"Sentadilla"` |
| `series` | `int` | `4` |
| `repeticiones` | `int` | `12` |
| `peso` | `float` | `40.0` |
| `descanso` | `int` | `90` |
| `activo` | `bool` | `True` |
| `objetivo` | `str` | `"fuerza"` |

## Las 15 reglas

Las 15 reglas en lenguaje natural están en el archivo [`reglas.txt`](./reglas.txt), y cumplen con:

| Requisito | Reglas que lo cubren |
|---|---|
| Condición simple (una sola evaluación) | 1, 2, 3, 4, 5 |
| Condición compuesta (Y / O) | 6, 7, 8, 9, 10 |
| Combinación de tipos de datos distintos | 11, 12, 13, 15 |

## Sintaxis formal de las reglas

```
SI <condicion> [Y|O <condicion>] ENTONCES <accion>

<condicion> ::= <variable> <operador> <valor>
<operador>  ::= ">" | "<" | ">=" | "<=" | "=="
<variable>  ::= identificador_en_minusculas
<valor>     ::= numero | "verdadero" | "falso" | texto_entre_comillas
<accion>    ::= identificador_en_minusculas
```

En la implementación de FitLang, `SI` y `ENTONCES` se representan con la palabra clave `si` y con el bloque `{ }` que sigue a la condición (en vez de escribir literalmente "entonces"). Opcionalmente puede usarse `sino { }` para definir una alternativa.

## Palabras reservadas

El detalle completo (significado y categoría de cada palabra) está en [`palabras_reservadas.md`](./palabras_reservadas.md).

Palabras clave: `rutina`, `ejercicio`, `series`, `repeticiones`, `peso`, `descanso`, `objetivo`, `activo`, `si`, `sino`.
Operadores lógicos: `y`, `o`.
Operadores relacionales: `>`, `<`, `>=`, `<=`, `==`.
Literales: `verdadero`, `falso`.

## Convención de escritura

- Las palabras reservadas se escriben en **minúsculas** (`si`, `sino`, `y`, `o`).
- Las variables se escriben en minúsculas y, si tienen más de una palabra, se separan con guion bajo (ej. `puerta_abierta`).
- Los valores de texto van siempre entre comillas dobles (ej. `"fuerza"`).
- Los operadores relacionales permitidos son: `>`, `<`, `>=`, `<=`, `==`.
- Cada bloque (`rutina`, `ejercicio`, `si`, `sino`) se delimita con llaves `{ }` y se indenta con 4 espacios.

## Ejemplos de sintaxis por funcionalidad

### Crear una rutina
```
rutina "Pierna" {
}
```

### Agregar un ejercicio
```
ejercicio "Sentadilla" {
}
```

### Definir series
```
series 4
```

### Definir repeticiones
```
repeticiones 12
```

### Definir peso
```
peso 40
```

### Definir descanso
```
descanso 90
```

### Estado activo
```
activo verdadero
activo falso
```

### Definir el objetivo
```
objetivo "fuerza"
objetivo "hipertrofia"
objetivo "resistencia"
```

### Condicional simple
```
si peso > 50 {
    reducir_peso 5
}
```

### Condicional simple con alternativa (si / sino)
```
si repeticiones >= 12 {
    aumentar_peso 5
} sino {
    mantener_peso
}
```

### Operador lógico y (AND)
```
si repeticiones >= 12 y activo == verdadero {
    aumentar_peso 5
}
```

### Operador lógico o (OR)
```
si peso > 50 o repeticiones > 15 {
    reducir_peso 5
}
```

### Detección de errores de tipo
```
series "muchas"   # ERROR: series debe ser un número entero.
series 4          # correcto
```

## Ejemplo completo

```
rutina "Pierna" {
    objetivo "fuerza"
    ejercicio "Sentadilla" {
        series 4
        repeticiones 12
        peso 40
        descanso 90
        activo verdadero
        si repeticiones >= 12 y activo == verdadero {
            aumentar_peso 5
        } sino {
            mantener_peso
        }
    }
}
```

## Licencia

Este proyecto está bajo la licencia del grupo 9. Consulta el archivo `LICENSE` para más detalles.
