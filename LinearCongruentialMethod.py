class LinearCongruentialMethod:
    def __init__(self, seed: int, k: int, g: int, c: int):
        self.seed = seed
        self.a = 1 + 4 * k
        self.m = 2 ** g
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
        print("Método Congruencial Lineal")
        self.seed = int(input("Semilla: "))
        k = int(input("Constante multiplicativa: a = 1 +4k. Ingrese el valor de k: "))
        g = int(input("Módulo: m = 2^g. Ingrese el valor de g: "))
        self.c = int(input("Constante aditiva c (Debe ser relativamente primo a m): "))
        n = int(input("Número de números pseudo aleatorios a generar: "))

        self.a = 1 + 4 * k
        self.m = 2 ** g

        print("\nPeríodo máximo (2^g) = m: ", self.m)

        numbers = self.random(n)

        print("\ni\tℤ[0, ∞)\t\tℝ [0, 1)")
        print("-" * 30)
        for i, num in enumerate(numbers):
            print(f"{i}\t{num * (self.m - 1)}\t\t\t{num:.6f}")
