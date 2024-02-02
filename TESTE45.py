from random import randint
import time
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
escolha = int(input('ESCOLHA A SUA JOGADA: '))
time.sleep(0.7)
print('JO')
time.sleep(0.7)
print('KEN')
time.sleep(0.7)
print('PO!!!')
time.sleep(0.5)
print('-=' * 11)
print('O computador jogou {}.'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[escolha]))
print('-=' * 11)
if computador == 0:
    if escolha == 0:
        print('EMPATOU!')
    elif escolha == 1:
        print('JOGADOR VENCEU!')
    elif escolha == 20:
        print('COMPUTADOR VENCEU')
    else:
        print('Opção inválida')
elif computador == 1:
    if escolha == 0:
        print('JOGADOR VENCEU!')
    elif escolha == 1:
        print('EMPATOU!')
    elif escolha == 2:
        print('JOGADOR PERDEU!')
    else:
     print('Opção inválida')
elif computador == 2:
    if escolha == 0:
        print('JOGADOR VENCEU!')
    elif escolha == 1:
        print('JOGADOR PERDEU!')
    elif escolha == 2:
        print('EMPATOU!')
    else:
     print('Opção inválida')
