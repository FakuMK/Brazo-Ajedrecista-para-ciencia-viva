import chess
import chess.engine

tablero = chess.Board()

ruta_stockfish = "/home/facu/stockfish/stockfish-ubuntu-x86-64"
motor = chess.engine.SimpleEngine.popen_uci(ruta_stockfish)

print("Jugas contra stockfish")
print("Escribi las jugadas tipo e2e4")
print("Si queres salir escribi salir")

while tablero.is_game_over() == False:
    print("")
    print(tablero)
    print("")

    jugada = input("Tu jugada: ")

    if jugada == "salir":
        break

    try:
        mov = chess.Move.from_uci(jugada)

        if mov in tablero.legal_moves:
            tablero.push(mov)
        else:
            print("esa jugada no vale")
            continue

    except:
        print("escribiste mal la jugada")
        continue

    if tablero.is_game_over():
        break

    respuesta = motor.play(tablero, chess.engine.Limit(time=0.1))
    print("stockfish juega:", respuesta.move)
    tablero.push(respuesta.move)

print("")
print("Partida terminada")
print(tablero)
print("Resultado:", tablero.result())

motor.quit()