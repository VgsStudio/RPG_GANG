from dados.dados import *

i = int(input("Quantas vezes? ")) #Max

n = 0 #Contador
S =  0 #Soma
falha = 0
sucesso = 0

while n < i:
    dado = dado20(0)
    print(dado)
    if dado <= 10:
        falha += 1
    else:
        sucesso += 1
    n += 1

pcfalha = falha/i * 100
pcsucesso = sucesso/i * 100

print("Após %i dados, sua porcentagem de fracasso é %.2f e de sucesso é %.2f" % (i,pcfalha, pcsucesso))