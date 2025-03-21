num = 0
soma = 0
boletim = []
nome = []
media = []
materia = []
desem_aluno = []

while(True):
   
    nome = (input(f"Digite o nome {num+1}º alunos: "))
    for m in range(1,6):
        nota=[]
        materia =(input(f"Digite a {m} materia: "))
        
        for b in range(1,5):
             print(f"BIMESTRE {b}")
             nota.append(int(input(f"Informe a nota: ")))
        nota.append(sum(nota)/4)
        desem_aluno.append( (materia, nota))
    boletim[nome] = desem_aluno
        
        
    opc= input("Deseja continuar cadastrando notas para o aluno? [S][N]: ")[0].upper()
    
    if(opc =="N"):
        break
    else:
        desem_aluno = []
    
print(boletim)

with open("notas.txt", "w") as arquivo:
    arquivo.write(f"{boletim}")