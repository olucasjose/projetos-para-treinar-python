import random
import os

def avaliar_resposta():
    global resposta
    if pergunta == resultado:
        resposta = 'certa'
        os.system("clear")
        print('Acertou!')
    else:
        print('Errou!')
        resposta = 'errada'

'''
lista_operadores: Define uma lista de operadores que podem ser utilizados nas operações apresentadas ao jogador.
resposta: SE estiver 'certa' o jogador avança para a próxima rodada, SENÃO, o loop é encerrado e o jogo termina na rodada atual.
rodada: Define o número da rodada inicial. reduzida em '-1' sempre que uma divisão com resto diferente de 0 é gerada.
'''

lista_operadores = ['+', '-', '×', '÷']
resposta = 'certa'
rodada = 1

'''
while (resposta == 'certa' ): Inicia o loop de operações apresentadas ao jogador. É encerrado quando um cálculo for respondido incorretamente.
print(str(rodada) + 'ª rodada:'): Informa a rodada atual.
rodada = rodada + 1: Incrementa o número de rodadas em '+1'.
'''

while (resposta == 'certa' ):
    print(str(rodada) + 'ª rodada:')
    rodada = rodada + 1

    fator_01 = random.randint(1, 10)
    operador = random.choice(lista_operadores)
    fator_02 = random.randint(1, 10)

    if operador == '+':
        pergunta = int(input(('%s %s %s = ' % (fator_01, operador, fator_02))))
        resultado = fator_01 + fator_02
        avaliar_resposta()

    if operador == '-':
        pergunta = int(input(('%s %s %s = ' % (fator_01, operador, fator_02))))
        resultado = fator_01 - fator_02
        avaliar_resposta()

    if operador == '×':
        pergunta = int(input(('%s %s %s = ' % (fator_01, operador, fator_02))))
        resultado = fator_01 * fator_02
        avaliar_resposta()

    if operador == '÷':
        if (fator_01 % fator_02) == 0:
            pergunta = int(
                input(('%s %s %s = ' % (fator_01, operador, fator_02))))
            resultado = fator_01 / fator_02
            avaliar_resposta()
        else:
            if rodada > 2:
                rodada = rodada - 1
                resposta = 'certa'
                os.system("clear")
                print('Acertou!')
            else:
                rodada = rodada - 1
                resposta = 'certa'
                os.system("clear")

linhas = 94 / 75

''' 
Ideias para recursos:
1. Após um erro, informar o resultado correto.
2. Mostrar estatísticas dos acertos: Porcentagem de acerto em cada tipo de operação, número de operações de cada tipo.
3. Cadastro para guardar nome de jogadores.
4. Histórico de maiores rankings de acertos.
5. Sistema onde o jogador possa definir o nível de dificuldade.
'''

'''
Obervações:
1. Acredito que é possível reduzir a quantidade de "if's" e encurtar o código se forem colocados "random.choice's" em alguns pontos estratégicos e/ou se forem criadas uma ou mais funções, mas vou focar em documentar o código antes de pensar nisso seriamente.
'''