P=input()
alfabeto='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
vogais={'A':alfabeto.find('A'),'E':alfabeto.find('E'),'I':alfabeto.find('I'),'O':alfabeto.find('O'),'U':alfabeto.find('U')}
consoantes = [x for x in alfabeto if x not in vogais.keys()]
sting=''
for x in consoantes:
    sting+=x
consoantes=sting
cifrado=''
def modulo(n):
    if n<0:
        return n*-1
    else:
        return n
for x in P:
    x=x.upper()
    if x not in vogais.keys():
        cifrado+=x
        index=alfabeto.find(x)
        distancia=None
        letraatual=None
        for y in vogais:
            if distancia is not None:
                if modulo(index-vogais[y])<distancia:
                    letraatual=y
                    distancia=modulo(index-vogais[y])
                elif modulo(index-vogais[y])==distancia:
                    if vogais[y]<vogais[letraatual]:
                        letraatual=y
                        distancia=modulo(index-vogais[y])
            else:
                distancia=modulo(index-vogais[y])
                letraatual=y
        cifrado+=letraatual
        if x!="Z":
            cifrado+=consoantes[consoantes.find(x)+1]
        else:
            cifrado+='Z'
    else:
        cifrado+=x
print(cifrado.lower())
