import math

class LinearCongruentialMethod:
    def __init__(self, seed: int, a: int, m: int, c: int):
        self.seed = seed
        self.a = a
        self.m = m
        self.c = c

    def generate(self, n:int) -> list[int]:
        """
        Genera n números pseudo aleatorios usando la fórmula recursiva:
        Xn+1 = (a * Xn + c) mod m
        Estos números son enteros y mayores a cero.
        :param n: Número de números pseudo aleatorios a generar
        :return: Lista de números pseudo aleatorios generados
        """
        numbers = []
        x_n = self.seed

        for _ in range(n):
            x_n = (self.a * x_n + self.c) % self.m
            numbers.append(x_n)

        return numbers

    def random(self, n:int) -> list[float]:
        """
        Genera n números pseudo aleatorios en el rango [0, 1)
        :param n: Número de números pseudo aleatorios a generar
        :return: Lista de números pseudo aleatorios generados
        """
        numbers = self.generate(n)
        return [x / (self.m - 1) for x in numbers]

    def execute(self) -> None:
        def validate_positive_integer(value: int, name: str) -> int:
            if value <= 0:
                raise ValueError(f"{name} debe ser un número entero positivo.")
            return value

        def validate_c(value: int, m: int) -> int:
            if value <= 0 or math.gcd(value, m) != 1:
                raise ValueError("c debe ser un número entero positivo y relativamente primo a m.")
            return value

        print("\nMétodo Congruencial Lineal")
        self.seed = validate_positive_integer(int(input("Semilla (X0, debe ser un número entero positivo): ")),
                                              "Semilla")
        k = validate_positive_integer(
            int(input("Constante multiplicativa: a = 1 + 4k. Ingrese el valor de k (entero positivo): ")), "k")
        g = validate_positive_integer(int(input("Módulo: m = 2^g. Ingrese el valor de g (entero positivo): ")), "g")
        self.m = 2 ** g
        self.c = validate_c(int(input("Constante aditiva c (Debe ser relativamente primo a m): ")), self.m)

        self.a = 1 + 4 * k

        print("\nPeríodo máximo (2^g) = m: ", self.m)

        numbers = self.random(n := int(input("Número de números pseudo aleatorios a generar: ")))

        print("\ni\tℤ[0, ∞)\t\tℝ [0, 1)")
        print("-" * 30)
        for i, num in enumerate(numbers):
            print(f"{i}\t{int(num * (self.m - 1)):>10}\t\t{num:.6f}")
