#Escreva um algoritmo que leia dois números inteiros e exiba a multiplicação entre eles seo primeiro número for par; caso contrário, exiba a soma dos números. 
v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
if(v1 % 2 == 0):
    a = v1 * v2
    print (a)
else:
    a = v1 + v2
    print (a)