from __future__ import annotations
import random
from typing import List, Set


class Carton:
    """
    Representa un cartón de bingo.

    Relación:
        - Agregación con Jugador
    """

    def __init__(self, palabra: str, max_num: int) -> None:
        if len(palabra) != 5 or len(set(palabra)) != 5:
            raise ValueError("La palabra debe tener 5 letras únicas")

        if max_num < 50 or max_num > 90 or max_num % 5 != 0:
            raise ValueError("El máximo debe ser entre 50 y 90 y múltiplo de 5")

        self.palabra: str = palabra.upper()
        self.max_num: int = max_num
        self.tarjeta: List[List[int]] = self._generar_tarjeta()
        self.marcados: Set[int] = set()

    def _generar_tarjeta(self) -> List[List[int]]:
        tamaño = self.max_num // 5
        dominios = [
            list(range(i * tamaño + 1, (i + 1) * tamaño + 1))
            for i in range(5)
        ]

        columnas = [random.sample(dom, 5) for dom in dominios]
        return [[columnas[j][i] for j in range(5)] for i in range(5)]

    def marcar_numero(self, numero: int) -> None:
        for fila in self.tarjeta:
            if numero in fila:
                self.marcados.add(numero)

    def verificar_bingo(self) -> bool:
        for fila in self.tarjeta:
            if all(n in self.marcados for n in fila):
                return True

        for col in range(5):
            if all(self.tarjeta[f][col] in self.marcados for f in range(5)):
                return True

        return False

    def faltantes_para_bingo(self) -> int:
        faltantes_min = 5

        for fila in self.tarjeta:
            faltantes = sum(1 for n in fila if n not in self.marcados)
            faltantes_min = min(faltantes_min, faltantes)

        for col in range(5):
            faltantes = sum(
                1 for f in range(5)
                if self.tarjeta[f][col] not in self.marcados
            )
            faltantes_min = min(faltantes_min, faltantes)

        return faltantes_min

    def contar_marcados(self) -> int:
        return len(self.marcados)

    def mostrar(self) -> None:
        print(" ".join(self.palabra))
        for fila in self.tarjeta:
            print(" ".join(f"{n:2}" for n in fila))
        print()