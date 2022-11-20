import random

def sortear_palavra(palavras):
    palavra_escolhida = random.choice(palavras).upper()
    return palavra_escolhida

palavras = ['Brasil','Alemanha','Catar','Holanda','Espanha','Equador','Argentina','Inglaterra']
palavra_escolhida = sortear_palavra(palavras)
letra_descobertas = ['_'] * len(palavra_escolhida)
erros = 0
palavra = ""

input('Aperte Enter para começar')
print('Dica: País')
while erros != 6 and '_' in letra_descobertas:

    letra = input('Digite uma letra: ').upper()
    
    if len(letra) > 1:
        print('Uma letra por vez. Tente de novo!')

    for x in range(len(palavra_escolhida)):
        if letra == palavra_escolhida[x]:
            letra_descobertas[x] = letra
            palavra = " ".join(letra_descobertas)

    if letra not in palavra_escolhida:
        erros += 1
        print(f'Você errou pela {erros} vez. Tente de novo!')

    if palavra != "":
        print(palavra)

if erros == 6:
    print('\nGAME OVER! Você perdeu.')
if '_' not in letra_descobertas:
    print('\nParabéns, você ganhou o jogo!')