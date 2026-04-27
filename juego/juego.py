from typing import List, Optional
from jugador.jugador import Jugador
from juego.bombo import Bombo


class Juego:
    """
    Director del juego

    Relación:
        - Composición con Bombo
        - Agregación con Jugador
    """

    def __init__(self, max_num: int) -> None:
        self.jugadores: List[Jugador] = []
        self.bombo: Bombo = Bombo(max_num)
        self.ganador: Optional[Jugador] = None

    def registrar_jugador(self, jugador: Jugador) -> None:
        self.jugadores.append(jugador)

    def jugar(self) -> None:
        print("\n=== INICIO DEL JUEGO ===")

        while not self.ganador:
            numero = self.bombo.sacar_numero()
            print(f"\nNúmero: {numero}")

            for j in self.jugadores:
                j.marcar(numero)

                if j.tiene_bingo():
                    self.ganador = j
                    break

        print(f"\nGANADOR: {self.ganador.nombre}")
        self.reporte_final()

    def reporte_final(self) -> None:
        print("\nHistorial:", self.bombo.historial)

        for j in self.jugadores:
            print(f"{j.nombre}: {j.total_marcados}")