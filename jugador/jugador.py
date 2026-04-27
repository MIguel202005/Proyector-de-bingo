from typing import List
from carton.carton import Carton


class Jugador:
    """
    Agregación con Carton
    """

    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self.cartones: List[Carton] = []
        self.total_marcados: int = 0

    def agregar_carton(self, carton: Carton) -> None:
        self.cartones.append(carton)

    def marcar(self, numero: int) -> None:
        for c in self.cartones:
            antes = c.contar_marcados()
            c.marcar_numero(numero)
            despues = c.contar_marcados()

            if despues > antes:
                print(f"{self.nombre} marcó {numero}")

            self.total_marcados += (despues - antes)

    def tiene_bingo(self) -> bool:
        return any(c.verificar_bingo() for c in self.cartones)

    def mostrar_cartones(self) -> None:
        print(f"Jugador: {self.nombre}")
        for i, c in enumerate(self.cartones, 1):
            print(f"Cartón {i}:")
            c.mostrar()