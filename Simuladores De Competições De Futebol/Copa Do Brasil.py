from asyncore import loop
import random

print('Simulação: Copa do Brasil 2022')


#Fase Semifinal



#Fase Final

print('\n')
 
finalista_01 = 'São Paulo' #input('Escolha um time: ')
finalista_02 = 'Palmeiras' #input('Escolha o adversário: ')

print('\n')

finalista_01_ida = random.randint(0,0)
finalista_02_ida = random.randint(0,0)

print('Jogo 1/2: ' + finalista_01 + ' ' + str(finalista_01_ida) + ' x ' + str(finalista_02_ida) + ' ' + finalista_02)

finalista_02_volta = random.randint(0,0)
finalista_01_volta = random.randint(0,0)

print('Jogo 2/2: ' + finalista_02 + ' ' + str(finalista_02_volta) + ' x ' + str(finalista_01_volta) + ' ' + finalista_01)

finalista_02_gols = finalista_02_ida + finalista_02_volta
finalista_01_gols = finalista_01_ida + finalista_01_volta

print('\n')

print('Placar agregado: ' + finalista_02 + ' ' + str(finalista_02_gols) + ' x ' + str(finalista_01_gols) + ' ' + finalista_01)

print('\n')

if finalista_02_gols < finalista_01_gols:
    print('O %s é campeão da Copa do Brasil 2022!' % finalista_01)
    campeao = finalista_01
if finalista_02_gols > finalista_01_gols:
    campeao = finalista_02
    print('O %s é campeão da Copa do Brasil 2022!' % finalista_02)
if finalista_02_gols == finalista_01_gols:
    print('O campeão será decidido nos penâltis.')

    print('\n')
    
    print('Primeira fase: 5 cobranças para cada time.')
    
    print('\n')

    #Primeira cobrança de pênaltis.
    finalista_01_penalti_01 = random.randint(0,0)
    finalista_02_penalti_01 = random.randint(0,0)
    print('1ª cobrança:')
    print(finalista_01 + ': ' + str(finalista_01_penalti_01))
    print(finalista_02 + ': ' + str(finalista_02_penalti_01))
    
    print('\n')
    
    #Segunda cobrança de pênaltis.
    finalista_01_penalti_02 = random.randint(0,0)
    finalista_02_penalti_02 = random.randint(0,0)
    print('2ª cobrança:')
    print(finalista_01 + ': ' + str(finalista_01_penalti_02))
    print(finalista_02 + ': ' + str(finalista_02_penalti_02))
    
    print('\n')

    #Terceira cobrança de pênaltis.
    finalista_01_penalti_03 = random.randint(0,0)
    finalista_02_penalti_03 = random.randint(0,0)
    print('3ª cobrança:')
    print(finalista_01 + ': ' + str(finalista_01_penalti_03))
    print(finalista_02 + ': ' + str(finalista_02_penalti_03))
    
    print('\n')
    
    #Quarta cobrança de pênaltis.
    finalista_01_penalti_04 = random.randint(0,0)
    finalista_02_penalti_04 = random.randint(0,0)
    print('4ª cobrança:')
    print(finalista_01 + ': ' + str(finalista_01_penalti_04))
    print(finalista_02 + ': ' + str(finalista_02_penalti_04))
    
    print('\n')
    
    #Quinta cobrança de pênaltis.
    finalista_01_penalti_05 = random.randint(0,0)
    finalista_02_penalti_05 = random.randint(0,0)
    print('5ª cobrança:')
    print(finalista_01 + ': ' + str(finalista_01_penalti_05))
    print(finalista_02 + ': ' + str(finalista_02_penalti_05))
    
    finalista_01_5cobrancas = finalista_01_penalti_01 + finalista_01_penalti_02 + finalista_01_penalti_03 + finalista_01_penalti_04 + finalista_01_penalti_05
    finalista_02_5cobrancas = finalista_02_penalti_01 + finalista_02_penalti_02 + finalista_02_penalti_03 + finalista_02_penalti_04 + finalista_02_penalti_05
    
    print('\n')

    #print('Placar nos pênaltis:')
    #print(finalista_01 + ': ' + str(finalista_01_5cobrancas))
    #print(finalista_02 + ': ' + str(finalista_02_5cobrancas))

    #print('\n')

    
    #print('Placar agregado: ' + finalista_02 + ' ' + str(finalista_02_gols) + ' x ' + str(finalista_01_gols) + ' ' + finalista_01)
    print('Placar provisório:')
    print(finalista_02 + ' ' + str(finalista_02_gols) + '(' + str(finalista_02_5cobrancas) + ')' ' x ' '(' + str(finalista_01_5cobrancas) + ')' + str(finalista_01_gols) + ' ' + finalista_01)
    #print(finalista_01 + ': ' + str(finalista_01_5cobrancas))
    #print(finalista_02 + ': ' + str(finalista_02_5cobrancas))
    
    
    print('\n')
    
    if finalista_02_5cobrancas < finalista_01_5cobrancas:
        print('O %s é campeão da Copa do Brasil 2022!' % finalista_01)
        campeao = finalista_01
    if finalista_02_5cobrancas > finalista_01_5cobrancas:
        campeao = finalista_02
        print('O %s é campeão da Copa do Brasil 2022!' % finalista_02)
    if finalista_02_5cobrancas == finalista_01_5cobrancas:
        print('Haja coração! Agora cada time têm apenas mais 1 pênalti.\nSe houver um novo empate, às crobranças continuarão\naté que um deles consiga superar o adversário.')

        print('\n')

        #Cobranças alternadas.
        placar_alternado = 0
        cobranca = 6
        repeticao = 0
        f01pa = 0
        f02pa = 0

        while (placar_alternado == 0):
            finalista_01_penalti_alternado = random.randint(0,1)
            if finalista_01_penalti_alternado == 1:
                f01pa = f01pa + 1
            finalista_02_penalti_alternado = random.randint(0,1)
            if finalista_02_penalti_alternado == 1:
                f02pa = f02pa + 1
            print(str(cobranca) + 'ª cobrança:')
            print(finalista_01 + ': ' + str(finalista_01_penalti_alternado))
            print(finalista_02 + ': ' + str(finalista_02_penalti_alternado))
            print('\n')
            cobranca = cobranca + 1
            repeticao = repeticao + 1
            placar_alternado = (finalista_01_penalti_alternado - finalista_02_penalti_alternado)
            
        
        #print('\n')

        if finalista_02_penalti_alternado < finalista_01_penalti_alternado:
            print('Fim de jogo!\n\nO %s é campeão da Copa do Brasil 2022!' % finalista_01)
            campeao = finalista_01
        if finalista_02_penalti_alternado > finalista_01_penalti_alternado:
            campeao = finalista_02
            print('Fim de jogo!\n\nO %s é campeão da Copa do Brasil 2022!' % finalista_02)

        print('Placar final:')
        #print(repeticao)
        print(f01pa)
        print(f02pa)
        print(finalista_02 + ' ' + str(finalista_02_gols) + '(' + str(finalista_02_5cobrancas + (finalista_02_penalti_alternado * repeticao)) + ')' ' x ' '(' + str(finalista_01_5cobrancas + (finalista_01_penalti_alternado * repeticao)) + ')' + str(finalista_01_gols) + ' ' + finalista_01)

        
 #           
 #           placar_alternado = finalista_01_penalti_alternado - finalista_02_penalti_alternado
#
 #           print(placar_alternado)
 #       
 #           print('\n')