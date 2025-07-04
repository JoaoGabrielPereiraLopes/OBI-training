S=int(input())
A=int(input())
B=int(input())
contagem=0
for x in range(A,B+1):
    x=str(x)
    soma=0
    for digito in x:
        soma+=int(digito)
    if soma==S:
        contagem+=1
print(contagem)