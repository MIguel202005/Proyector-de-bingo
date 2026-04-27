from carton.carton import Carton
from carton.carton_doble import CartonDoble
from jugador.jugador import Jugador
from juego.juego import Juego


def main() -> None:
    palabra = "BINGO"
    max_num = 75

    juego = Juego(max_num)

    j1 = Jugador("Brahian")
    j2 = Jugador("Carlos")
    j3 = Jugador("Ana")

    j1.agregar_carton(Carton(palabra, max_num))
    j2.agregar_carton(CartonDoble(palabra, max_num))
    j3.agregar_carton(Carton(palabra, max_num))

    juego.registrar_jugador(j1)
    juego.registrar_jugador(j2)
    juego.registrar_jugador(j3)

    print("\nCARTONES INICIALES\n")
    for j in juego.jugadores:
        j.mostrar_cartones()

    juego.jugar()


if __name__ == "__main__":
    main()