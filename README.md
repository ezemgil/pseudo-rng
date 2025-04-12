# Generador de números pseudoaleatorios
Este repositorio contiene un generador de números pseudoaleatorios en Python. El generador utiliza los métodos
**Congruencial Lineal** (LCG) y **Congruencial multiplicativo** (MCG) para generar números pseudoaleatorios.

El repositorio contiene clases para implementar los métodos Congruencial Lineal y Congruencial Multiplicativo,
concretamente `LinearCongruentialMethod.py` y `MultiplicativeCongruentialMethod.py`, respectivamente. Ambas clases
tienen un método `execute()` que solicita al usuario los parámetros necesarios para configurar y ejecutar
el generador correspondiente. El archivo `main.py` ejecuta ambos métodos llamando a `execute()` de cada clase.

## Método Congruencial Lineal (LCG)
El método congruencial lineal genera una secuencia de números enteros utilizando la siguiente ecuación recursiva:

$X_{i+1} = (a \cdot X_i + c) \mod m \quad \text{para } i = 0, 1, 2, 3, \dots, n$

Donde:
- $X_0$ es la semilla.
- $a$ es la constante multiplicativa.
- $c$ es la constante aditiva.
- $m$ es el módulo.

Todos estos valores deben ser números enteros positivos. La ecuación genera una secuencia de números enteros. Para
obtener números pseudoaleatorios en el intervalo $(0, 1)$, se utiliza la siguiente fórmula:

$\text{rnd}_i = \frac{X_i}{m - 1} \quad \text{para } i = 1, 2, 3, \dots, n$

Para que el algoritmo alcance el período máximo $N$, los parámetros deben cumplir las siguientes condiciones:
- $m = 2^g$, donde $g$ es un número entero positivo.
- $a = 1 + 4 \cdot k$, donde $k$ es un número entero positivo.
- $c$ debe ser relativamente primo a $m$.

Bajo estas condiciones, es posible alcanzar un período máximo $N = m = 2^g$.

## Método Congruencial Multiplicativo (MCG)
El método congruencial multiplicativo se deriva del método congruencial lineal cuando la constante $ c = 0 $. Su ecuación recursiva es:

$X_{i+1} = (a \cdot X_i) \mod m \quad \text{para } i = 0, 1, 2, 3, \dots, n$

Donde:
- $ X_0 $ es la semilla.
- $ a $ es la constante multiplicativa.
- $ m $ es el módulo.

Este método tiene la ventaja de requerir una operación menos en comparación con el método congruencial lineal. Al igual que el otro método, los parámetros deben ser números enteros positivos. Además, los números generados deben transformarse para que estén en el intervalo $ (0, 1) $:

$\text{rnd}_i = \frac{X_i}{m - 1} \quad \text{para } i = 1, 2, 3, \dots, n$

Para que el algoritmo alcance el período máximo $ N $, los parámetros deben cumplir las siguientes condiciones:
- $ m = 2^g $, donde $ g $ es un número entero positivo.
- $ a = 3 + 8 \cdot k $ o $ a = 5 + 8 \cdot k $, donde $ k = 0, 1, 2, 3, \dots $.
- $ X_0 $ debe ser un número impar.

Bajo estas condiciones, es posible alcanzar un período máximo $ N = \frac{m}{4} = 2^{g-2} $. [1]
> [1] **Banks J, Carson JS, Nelson BL, Nicol DM**: *“Simulación de Sistemas de Eventos Discretos”*