num=int(input("digite seu número: "))
contagem=0
while num>0:
    num=num//10
    contagem+=1
print(contagem)
