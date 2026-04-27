from carton.carton import Carton


class CartonDoble(Carton):
    """
    Representa un cartón doble.

    Relación:
        - Herencia de Carton
    """

    def __init__(self, palabra: str, max_num: int) -> None:
        super().__init__(palabra, max_num)
        self.carton2: Carton = Carton(palabra, max_num)

    def marcar_numero(self, numero: int) -> None:
        super().marcar_numero(numero)
        self.carton2.marcar_numero(numero)

    def verificar_bingo(self) -> bool:
        return super().verificar_bingo() or self.carton2.verificar_bingo()

    def mas_cercano_a_bingo(self) -> int:
        f1 = self.faltantes_para_bingo()
        f2 = self.carton2.faltantes_para_bingo()
        return 1 if f1 <= f2 else 2

    def mostrar(self) -> None:
        print("Cartón 1:")
        super().mostrar()
        print("Cartón 2:")
        self.carton2.mostrar()