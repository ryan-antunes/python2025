#cpf = [5,5,6,8,9,1,5,5,8,0,2]
cpf = str(input("Digite o seu cpf: \n"))
verd = [ ]
for n in cpf:
    if n in "0123456789":
        valor = int(n)
        verd.append(valor)
multi = cpf[0]*10, cpf[1]*9, cpf[2]*8, cpf[3]*7, cpf[4]*6, cpf[5]*5, cpf[6]*4, cpf[7]*3, cpf[8]*2
soma = sum(multi)
divisao = soma%11
if (divisao<2):
    v1 = 0
else:
    v1 = 11-divisao
multi2 = cpf[0]*11, cpf[1]*10, cpf[2]*9, cpf[3]*8, cpf[4]*7, cpf[5]*6, cpf[6]*5, cpf[7]*4, cpf[8]*3, cpf[9]*2
soma2 = sum(multi2)
divisao2 = soma2/11
if (divisao2<2):
    v2 = 11-divisao2
print (cpf)
print (multi)
print (soma)
print (v1)