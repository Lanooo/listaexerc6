m =  int(input("Informe a média (0 a 10): "))
f = int(input("Informe a frequência (0 a 100): "))

if f < 75:
    print("Você foi reprovado")
    
if (f >= 75) and (m < 7):
    print("Você está de recuperação")
    
if (f >= 75) and (m> 7):
    print("Você foi aprovado")
