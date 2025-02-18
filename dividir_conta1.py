# Escreva um programa que receba o valor dos produtos
# somando todos, gere o valor de consumo total
# de uma mesa, se o pagamento será feito de forma integral ou dividido
# a quantidade de pessoas que tem na mesa 
# e faça o cálculo de quanto cada pessoa deve pagar. 
# Acrescentando os 10% do garçom, caso ela queira realizar 
# o pagamento. 

id_mesa = int(input("Digite a identificação da mesa: "))
#variável de condição para executar o programa
consumo = (input("Há consumo para adicionar a compra? \n Digite S para SIM e N para NÃO! ")).upper() 

#Laço de repetição para iniciar o programa

while consumo == "S":
    valor_consumo = float(input("Entre com o valor consumido pela mesa %d: " % id_mesa))
    gorjeta_garcom = (valor_consumo*1.1)
    print ("O valor consumido foi de R$%.2f!" %valor_consumo)
    print ("O valor com a gorjeta do garçom é R$%.2f. Deseja incluir? " % gorjeta_garcom)
    pagar_gorjeta = input("Digite S para SIM, N para NÃO.").upper()

    #condição com pagamento dos 10%
    if pagar_gorjeta == "S":
        dividir_consumo = (input ("Deseja dividir o valor entre os consumidores da mesa? \nDigite S para SIM e N para NÃO: ")).upper()
        # condição para dividir a conta entre participantes com opção "S".
        if dividir_consumo == "S":
            quantidade_pessoas = int(input("Deseja dividir com quantas pessoas? "))
            print("O valor total com a gorjeta do garçom é de R$%.2f." % gorjeta_garcom)
            print ("O valor para cada pessoa é de %.2f: " % (gorjeta_garcom / quantidade_pessoas))
        else:
            print("O valor a pagar é de R$%.2f." % gorjeta_garcom)
    else:
        dividir_consumo = (input ("Deseja dividir o valor entre os consumidores da mesa? \nDigite S para SIM e N para NÃO: ")).upper()
        # condição para dividir a conta entre participante com opção "N" para a gorjeta. 
        if dividir_consumo == "N":
            print("O valor total é de %.2f." % valor_consumo)
        else:
            print("O valor a pagar é de R$%.2f. " % valor_consumo)
    consumo = (input("Há consumo para adicionar a compra? \n Digite S para SIM e N para NÃO! ")).upper()
    if consumo == "N":
        print("O programa será encerrado!")
        break
print ("Fim do programa.")
