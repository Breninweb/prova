#1. Escreva um programa para ler 3 valores inteiros e escrever o maior
#deles. Considere que o usuário não informará valores iguais. (1,0)


primeiroValor = int(input('digite o primeiro valor: '))
segundoValor = int(input('digite o segundo valor: '))
terceiroValor = int(input('digite o terceiro valor: '))

if primeiroValor > segundoValor and primeiroValor > terceiroValor:
    print(primeiroValor)
elif segundoValor > primeiroValor and segundoValor > terceiroValor:
    print(segundoValor)
else:
    print(terceiroValor)

#Leia a idade e o tempo de serviço de um trabalhador e escreva se ele
#pode ou não se aposentar. As condições para aposentadoria são: (1,5)
#a. Ter pelo menos 65 anos;
#b. Ou ter trabalhado pelo menos 30 anos;
#c. Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos


idade = int(input("Qual a sua idade? "))

tempo = int(input("Quanto tempo voce trabalhou? "))


if idade >= 65:
    print("Pode aposentar")

if tempo >= 30:
    print("Pode aposentar")

if idade >= 60 and tempo >= 25:
    print("Pode aposentar")
else:
    print("Você não pode se aposentar ainda, vai trabalhar")


#Faça um programa que seja semelhante ao jogo da forca, mas com uma
#única letra. A letra que o usuário deve adivinhar deve ser definida no
#código do programa. O usuário tem 5 chances de acertar a letra. O
#programa finaliza sua execução quando o usuário acerta a letra ou
#quando acabam suas chances. (1,0)

vidas = 5

forca = 'a'

while vidas > 0:
    jogador = str(input("Tente adivinhar a letra: "))
    if forca == jogador:
        print("Voce venceu")
        break
    else:
        vidas -= 1
        print()
if vidas == 0:
    print("Acabou as tentativas")


#Escreva um programa que apresente quatro opções:
#(1) consulta saldo,
#(2) saque e
#(3) depósito e
#(4) sair.
#O saldo deve iniciar em R$ 0,00.
#A cada saque ou depósito o valor do saldo deve ser atualizado. (1,5)


saldo = 0
saque = 0
deposito = 0
acao = 0

ativar = int(input("Aperte 1 para ligar: "))
print("")

while ativar == 1:
    print("Aperte 1 para ver seu saldo")
    print("Aperte 2 para sacar")
    print("Aperte 3 para depositar")
    print("Aperte 4 para desligar")
    print("")

    acao = int(input("O que deseja fazer? "))
    print("")

    if acao == 1:
        print("Seu saldo: ",saldo)
        print("")
    elif acao == 2:
        saque = int(input("Quanto deseja sacar? "))
        saldo -= saque
        print("Saque efetuado com sucesso",saldo)
        print("")
    elif acao == 3:
        deposito = int(input("Quanto deseja depositar? "))
        saldo += deposito
        print("Deposito efetuado com sucesso",saldo)
        print("")
    elif acao == 4:
        print("Desligando...")
        ativar = 0
    else:
        print("Não entendi")
        break

