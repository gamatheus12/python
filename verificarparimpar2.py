numero = int(input('Digite um número para saber se é par ou impar:'))
resto = numero % 2

if resto == 0:
    print(f' {numero} é par')
else:
    print(f' {numero} é impar')