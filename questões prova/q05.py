repeticoes=int(input("Digite quantidade de repetições: "))
soma=0
valor=[]
for i in range(1,repeticoes+1):
    num=int(input(f"digite o valor {i}: "))
    soma+=num
    valor.append(num)
media=soma/repeticoes
maior=max(valor)
menor=min(valor)
print(f"a soma total é {soma}")
print(f"a média é {media}")
print(f"maior valor é {maior}")
print(f"o menor valor é {menor}")
cont=0
for g in valor:
    if i>media:
        cont+=1
print(f"a quantidade de valores acima da média é {cont}")


