#!/usr/bin/python3
# quatro operações basicas

a=float(input("digite um numero\n"))
b=float(input("digite outro numero\n"))
op=input("digite a operação\n")
if (op==1 or (op=='1')):
    soma=a+b
    print('soma: {}'.format(soma))
elif (op==2 or (op=='2')):
    sub=a-b
    print('subtração: {}'.format(sub))
elif (op==3 or (op=='3')):
    div=a/b
    resto=a%b
    print('divisão: {}'.format(div))
    print ('resto: {}'.format(resto))
elif (op==4 or (op=='4')):
    mult=a*b
    print('multiplicação: : {}'.format(mult))
else:
    print("opcao não exite")
