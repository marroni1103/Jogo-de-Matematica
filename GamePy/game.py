from models.calcular import Calcular

def main() -> None: # aqui poderia ser qualquer nome a classe
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe a dificuldade desejada (1, 2, 3 ou 4): '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Voçê tem {pontos} ponto(s)')

    continuar: int = int(input('Deseja continuar no jogo? (1 - sim, 0 - não)'))

    if continuar:
        jogar(pontos)
    else:
        print(f'Voçê finalizou com {pontos} ponto(s).')
        print('Até a proxima!!')


if __name__ == '__main__':
    main()