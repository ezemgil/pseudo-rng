class MultiplicativeCongruentialMethod:
    def __init__(self, seed: int, a: int, m: int):
        self.seed = seed
        self.a = a
        self.m = m

    def generate(self, n: int) -> list[int]:
        """
        Genera n números pseudo aleatorios usando la fórmula recursiva:
        Xn+1 = (a * Xn) mod m
        :param n: Número de números pseudo aleatorios a generar
        :return: Lista de números pseudo aleatorios generados
        """
        numbers = []
        x_n = self.seed

        for _ in range(n):
            x_n = (self.a * x_n) % self.m
            numbers.append(x_n)

        return numbers

    def random(self, n: int) -> list[float]:
        """
        Genera n números pseudo aleatorios en el rango [0, 1)
        :param n: Número de números pseudo aleatorios a generar
        :return: Lista de números pseudo aleatorios generados
        """
        numbers = self.generate(n)
        return [x / (self.m - 1) for x in numbers]

    def execute(self) -> None:
        def validate_positive_odd_integer(value: int, name: str) -> int:
            if value <= 0 or value % 2 == 0:
                raise ValueError(f"{name} debe ser un número entero positivo e impar.")
            return value

        def validate_a_choice(choice: int, k: int) -> int:
            if choice == 1:
                return 3 + 8 * k
            elif choice == 2:
                return 5 + 8 * k
            else:
                raise ValueError("Opción inválida para 'a'. Elija 1 o 2.")

        print("Método Congruencial Multiplicativo")
        self.seed = validate_positive_odd_integer(
            int(input("Semilla (X0, debe ser un número impar): ")), "Semilla"
        )

        k = int(input("Constante multiplicativa: a = 3 + 8k ó a = 5 + 8k. Ingrese el valor de k (entero positivo): "))
        a_choice = int(input("Elija la fórmula para 'a': (1) a = 3 + 8k, (2) a = 5 + 8k: "))
        self.a = validate_a_choice(a_choice, k)

        g = int(input("Módulo: m = 2^g. Ingrese el valor de g (entero positivo): "))
        if g <= 0:
            raise ValueError("g debe ser un número entero positivo.")
        self.m = 2 ** g

        n = int(input("Número de números pseudo aleatorios a generar: "))
        if n <= 0:
            raise ValueError("El número de valores a generar debe ser un entero positivo.")

        print("\nPeríodo máximo esperado (m/4) = 2^(g-2): ", 2 ** (g - 2))

        numbers = self.random(n)

        print("\ni\tℤ[0, ∞)\t\tℝ [0, 1)")
        print("-" * 30)
        for i, num in enumerate(numbers):
            print(f"{i:<5}{int(num * (self.m - 1)):>10}\t\t{num:.6f}")