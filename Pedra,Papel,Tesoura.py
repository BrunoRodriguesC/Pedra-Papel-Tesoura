import os
from random import choice

jogador_vitorias = 0
maquina_vitorias = 0


def Opcao_jogador():
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else:
        print("opcao invalida. tente novamente")
        Opcao_jogador()


def Opcao_Maquina():
    esc_Maquina = choice(["pedra", "papel", "tesoura"])
    return esc_Maquina

def Jogo():
    while True:
        global jogador_vitorias
        global maquina_vitorias
        print(30 * "-")
        esc_jogador = Opcao_jogador()
        esc_Maquina = Opcao_Maquina()
        print(30 * "-")

        if (esc_jogador == "pedra") and (esc_Maquina == "tesoura") \
            or (esc_jogador == "papel") and (esc_Maquina == "pedra") \
                or (esc_jogador == "tesoura") and (esc_Maquina == "papel"): \
                # jogador ganha
            print(f"Joagador escolheu: {esc_jogador} e a Maquina escolheu: \
{esc_Maquina} Resultado: Voce ganhou!")
            jogador_vitorias += 1
        elif esc_jogador == esc_Maquina:
            # Empate
            print(f"Joagador escolheu: {esc_jogador} e a Maquina escolheu: \
{esc_Maquina} Resultado: Empate")
        else:
            # Maquina ganha
            print(f"Joagador escolheu: {esc_jogador} e a Maquina escolheu: \
{esc_Maquina} Resultado: Voce perdeu")
            maquina_vitorias += 1

        print(30 * "-")
        print(f"Vitorias do jogador: {jogador_vitorias}")
        print(f"Vitorias da Maquina: {maquina_vitorias}")
        print(30 * "-")

        esc_jogador = input("Voce quer jogar novamente? ")
        if esc_jogador in ["SIM", "sim", "Sim", "s", "S"]:
            os.system("cls")
            return Jogo()
        elif esc_jogador in ["NAO", "nao", "Nao", "n", "N"]:
            break
        else:
            break
Jogo()