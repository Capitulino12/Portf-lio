from random import randint
from time import sleep
itens = ('Pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua escolha: '))
print('PROCESSANDO...')
sleep(2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 12)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('JOGADOR PERDEU')
elif computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
    elif jogador == 0:
        print('JOGADOR PERDEU')
elif computador == 2:
    if jogador == 1:
        print('JOGADOR PERDEU')
    elif jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('JOGADOR VENCEU')
else:
    print('JOGADA INVALIDA')
