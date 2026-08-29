# FitLang

**FitLang** es un lenguaje de dominio específico (DSL) diseñado para describir rutinas de entrenamiento de forma simple, estructurada y legible. Permite crear rutinas, definir ejercicios, series, repeticiones, peso, descanso, objetivos, y tomar decisiones automáticas sobre el rendimiento del usuario.

## Qué puede hacer FitLang

- Crear rutinas de entrenamiento.
- Agregar ejercicios a una rutina.
- Definir series, repeticiones, peso y descanso.
- Establecer un objetivo (fuerza, hipertrofia, resistencia).
- Saber si un ejercicio está activo.
- Evaluar el rendimiento del usuario.
- Decidir automáticamente si se debe **aumentar**, **disminuir** o **mantener** el peso.

## Tipos de datos

| Tipo      | Ejemplo              |
|-----------|-----------------------|
| Texto     | `"Sentadilla"`         |
| Entero    | `4`, `12`, `90`        |
| Número    | `40`, `40.5`           |
| Booleano  | `verdadero`, `falso`   |

## Cobertura de condiciones

El lenguaje procesa distintos tipos de condiciones. Se distribuyen así entre las 15 reglas:

| Requisito | Reglas que lo cubren |
|---|---|
| Condición simple (una sola evaluación, sin `y`/`o`) | 8, 9, 14 |
| Condición compuesta (`y` / `o`) | 10, 11, 12, 13 |
| Combinación numérico + booleano | 10, 12 |
| Combinación texto + booleano | 13 |

## Reglas del lenguaje

### 1. Crear una rutina
```
rutina "Pierna" {
}
```

### 2. Agregar un ejercicio
```
ejercicio "Sentadilla" {
}
```

### 3. Definir series
```
series 4
```

### 4. Definir repeticiones
```
repeticiones 12
```

### 5. Definir peso
```
peso 40
```

### 6. Definir descanso
```
descanso 90
```

### 7. Estado activo
```
activo verdadero
activo falso
```

### 8. Condicional simple
```
si peso > 50 {
    aumentar_peso 5
}
```

### 9. Condicional simple con alternativa (si / sino)
```
si repeticiones >= 12 {
    aumentar_peso 5
} sino {
    mantener_peso
}
```
Evalúa una sola condición (`repeticiones >= 12`), solo que define qué hacer también cuando no se cumple.

### 10. Operador lógico `y` (AND)
```
si repeticiones >= 12 y activo == verdadero {
    aumentar_peso 5
}
```
Condición compuesta. Combina numérico (`repeticiones`) con booleano (`activo`).

### 11. Operador lógico `o` (OR)
```
si peso > 50 o repeticiones > 15 {
    reducir_peso 5
}
```
Condición compuesta.

### 12. Combinar número + booleano
```
si peso > 30 y activo == verdadero {
    aumentar_peso 5
}
```
Condición compuesta. Combina numérico (`peso`) con booleano (`activo`).

### 13. Combinar texto + booleano
```
si objetivo == "fuerza" y activo == verdadero {
    aumentar_peso 5
}
```
Condición compuesta. Combina texto (`objetivo`) con booleano (`activo`).

### 14. Definir el objetivo
```
objetivo "fuerza"
objetivo "hipertrofia"
objetivo "resistencia"
```

También puede usarse en una condición simple:
```
si objetivo == "hipertrofia" {
    aumentar_peso 2
}
```

### 15. Detección de errores de tipo
```
series "muchas"   ERROR: series debe ser un número entero.
series 4          correcto
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
