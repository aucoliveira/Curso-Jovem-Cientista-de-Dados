import random

def computer():
    escolha = random.randint(1,3)
    # ou posso ultilizar a função choice
    '''
        opcao = [1,2,3]
        escolha = random.choice(opcao)
    '''
    if escolha == 1:
        return 'Pedra'
    elif escolha == 2:
        return 'Papel'
    else:
        return 'Tesoura'

def jogo():
    print('Escolha uma opção(1, 2, 3 ou 4): ')
    print('1 - Pedra;')
    print('2 - Papel;')
    print('3 - Tesoura;')
    print('4 - Sair;')
    opcao = input('\nEscolha uma opção: ')

    if opcao == '':
        opcao =0
    opcao =  int(opcao)

    while opcao < 1 or opcao >4:
        print('\n\033[91m Opção inválida\033[m')
        if opcao == '':
            opcao = 0
        opcao = int(opcao)
        if opcao < 1 or opcao >4:
            opcao = int(input('Digite  uma opção VALIDA: '))
    return opcao

chamando_jogo = jogo()

while chamando_jogo != 4:
    jogadas_user = []
    rodadas = 0
    if rodadas >= 5:
        dado = [1, 2, 3]
        computador_escolha = random.choices(dado, weights=jogadas_user)

        if computador_escolha == 1:
            computador = 'Pedra'
        elif computador_escolha == 2:
            computador = 'Papel'
        else:
            computador = 'Tesoura'        

        if chamando_jogo == 1:
            user = 'Pedra'
            print('Você escolheu Pedra')
            print(f'O computador escolheu {computador}')

            if computador == 'Tesoura':
                print(f'Parabéns, você ganhou!')
            elif computador == 'Papel':
                print(f'Que pena, você perdeu!')
            else:
                print(f'Empate, joguem novamente')

        elif chamando_jogo == 2:
            user = 'Papel'
            
            print('Você escolheu Papel')
            print(f'O computador escolheu {computador}')

            if computador == 'Tesoura':
                print(f'Que pena, você perdeu!') 
            elif computador == 'Pedra':
                print(f'Parabéns, você ganhou!')
            else:
                print(f'Empate, joguem novamente')  

        elif chamando_jogo == 3:
            user = 'Tesoura'
            
            print('Você escolheu Tesoura')
            print(f'O computador escolheu {computador}')

            if computador == 'Pedra':
                print(f'Que pena, você perdeu!') 
            elif computador == 'Papel':
                print(f'Parabéns, você ganhou!')
            else:
                print(f'Empate, joguem novamente')
        
        

    if chamando_jogo == 1:
        user = 'Pedra'
        computador = computer()
        print('Você escolheu Pedra')
        print(f'O computador escolheu {computador}')

        if computador == 'Tesoura':
            print(f'Parabéns, você ganhou!')
        elif computador == 'Papel':
            print(f'Que pena, você perdeu!')
        else:
            print(f'Empate, joguem novamente')

    elif chamando_jogo == 2:
        user = 'Papel'
        computador = computer()
        print('Você escolheu Papel')
        print(f'O computador escolheu {computador}')

        if computador == 'Tesoura':
            print(f'Que pena, você perdeu!') 
        elif computador == 'Pedra':
            print(f'Parabéns, você ganhou!')
        else:
            print(f'Empate, joguem novamente')  

    elif chamando_jogo == 3:
        user = 'Tesoura'
        computador = computer()
        print('Você escolheu Tesoura')
        print(f'O computador escolheu {computador}')

        if computador == 'Pedra':
            print(f'Que pena, você perdeu!') 
        elif computador == 'Papel':
            print(f'Parabéns, você ganhou!')
        else:
            print(f'Empate, joguem novamente')
        rodadas += 1
        jogadas_user.append(chamando_jogo)
    chamando_jogo = jogo()

print('Tchau, volte sempre.')