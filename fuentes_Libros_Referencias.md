# Fuentes bibliográficas consultadas — FitLang

Este documento registra de qué libro, capítulo y página se obtuvo cada concepto teórico utilizado en el proyecto. Los números de página corresponden a las ediciones consultadas.

## Fuentes consultadas

**[H]** Hopcroft, J. E., Motwani, R., & Ullman, J. D. *Teoría de autómatas, lenguajes y computación*. Pearson Addison Wesley.

**[G]** Giró, J., Vázquez, J., Meloni, B., & Constable, L. *Lenguajes formales y teoría de autómatas*. Alfaomega.

## Tabla de trazabilidad

| Concepto utilizado | Fuente | Capítulo | Página aprox. | Cómo se aplicó en FitLang |
|---|---|---|---|---|
| Definición de alfabeto, cadena y lenguaje como conjunto de cadenas | [H] | Cap. 1 — Introducción a los autómatas | p. 5 | Sirvió para definir el alfabeto Σ de FitLang (palabras reservadas, operadores, literales) y entender cada regla válida como una "cadena" que pertenece al lenguaje del sistema. |
| Definición formal de lenguaje y su construcción a partir de un alfabeto | [G] | Cap. 1 — Introducción a la teoría de la computación | p. 1 | Confirmó el enfoque de tratar FitLang como un lenguaje formal desde el inicio, justificando por qué necesita reglas y vocabulario definidos con precisión. |
| Definición de gramática G = (V, Σ, R, S) y reglas de producción | [H] | Cap. 5 — Lenguajes y gramáticas independientes del contexto | p. 179 | Fue la base directa para escribir la gramática formal de FitLang en notación BNF (`<condicion> ::= <variable> <operador> <valor>`, etc.). |
| Presentación de gramáticas formales y notación de producción | [G] | Cap. 2 — Gramáticas y lenguajes formales | p. 21 | Ayudó a redactar las reglas de producción de FitLang de forma consistente y a decidir qué símbolos son terminales (palabras reservadas, operadores) y cuáles no terminales (`<condicion>`, `<accion>`). |
| Concepto de autómata finito determinista como reconocedor de cadenas | [H] | Cap. 2 — Autómatas finitos | (verificar página en la edición del grupo) | Fundamentó el diseño del analizador léxico de FitLang: el proceso de reconocer palabras clave, identificadores y operadores carácter por carácter antes de interpretarlos. |
| Autómatas finitos deterministas y su aplicación como base de analizadores léxicos | [G] | Cap. 3 — Máquinas secuenciales y autómatas finitos deterministas | p. 119 | Se usó para plantear el diagrama de estados que tokeniza una regla de FitLang (por ejemplo, separar `si repeticiones >= 12` en los tokens `si`, `repeticiones`, `>=`, `12`). |
| Autómatas finitos no deterministas y su equivalencia con los deterministas | [G] | Cap. 4 — Autómatas finitos no deterministas | p. 179 | Ayudó a verificar que, aunque el analizador léxico se piense de forma más flexible (varias transiciones posibles para un mismo símbolo), siempre puede convertirse en un autómata determinista equivalente para implementarlo en Java. |
| Clasificación de lenguajes según la jerarquía de Chomsky (regular, libre de contexto, sensible al contexto, recursivamente enumerable) | [H] | Distribuido en los Cap. 2–4 (regulares), Cap. 5–7 (libres de contexto) y Cap. 8–9 (máquinas de Turing) | — (concepto transversal, sin una única página) | Permitió justificar por qué FitLang no puede describirse solo con expresiones regulares (por sus bloques anidados `rutina { ejercicio { si { } } }`) y requiere una gramática libre de contexto. |
| Presentación unificada de lenguajes y gramáticas según la tipificación de Chomsky | [G] | Cap. 2 — Gramáticas y lenguajes formales | p. 21 | Se usó para clasificar formalmente a FitLang como un lenguaje de Tipo 2 (libre de contexto) dentro de la jerarquía de Chomsky. |
| Vínculo conceptual entre autómatas/gramáticas formales y la construcción de compiladores e intérpretes | [G] | Apéndice A — Conceptos de compiladores e intérpretes | (verificar página en la edición del grupo) | Sirvió de guía para estructurar el futuro intérprete de FitLang en Java en las fases clásicas: análisis léxico (autómata) → análisis sintáctico (gramática) → ejecución de la acción. |

