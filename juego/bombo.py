import random
from typing import List


class Bombo:
    """
    Composición con Juego
    """

    def __init__(self, max_num: int) -> None:
        self.numeros: List[int] = list(range(1, max_num + 1))
        self.historial: List[int] = []

    def sacar_numero(self) -> int:
        if not self.numeros:
            raise ValueError("No hay más números")

        numero = random.choice(self.numeros)
        self.numeros.remove(numero)
        self.historial.append(numero)
        return numero