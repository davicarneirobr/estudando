#soma de sequencia de numeros dados pelo usuario
print ("Digite uma sequencia de valores terminada por zero")
soma = 0
valor = 1
while valor != 0:
    valor=float(input("Digite um valor a ser somado:"))
    soma = soma + valor
print ("A soma dos valores digitados é", soma)