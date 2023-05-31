f=open("gramatica.in","r")
n=int(f.readline())
gramatica = {}
linie = f.readline().split()
neterminal = linie[0]
plecare = linie[0]
aux = linie[1].split("|")

line = f.readline()
while line:
    gramatica[neterminal] = []
    for i in range(len(aux)):
        gramatica[neterminal].append(aux[i])

    linie = line.split()
    neterminal = linie[0]
    aux = linie[1].split("|")
    line = f.readline()

gramatica[neterminal] = []
for i in range(len(aux)):
    gramatica[neterminal].append(aux[i])

print(gramatica)


terminale=[]
for litera in gramatica:
    for stare in gramatica[litera]:
        if stare=='~' or ((len(stare)==1 and (stare>= 'a' and stare <= 'z'))):
            terminale.append(litera)

print(terminale)

cuvinte=[]
for litera in gramatica[plecare]:
    cuvinte.append(litera)
print(cuvinte)

for i in range(1,n):
    L_update = []
    for cuvant in cuvinte:
        if(cuvant[len(cuvant)-1]>= "A" and cuvant[len(cuvant)-1]<="Z"):
            for litera in gramatica[cuvant[len(cuvant)-1]]:
                L_update.append(cuvant[:len(cuvant)-1]+litera)
    cuvinte=L_update

print(cuvinte)


cuvinte_ok = []
for i in cuvinte:
    if(i[len(i)-1] in terminale):
        cuvinte_ok.append(i[:len(i)-1])
print(cuvinte_ok)
