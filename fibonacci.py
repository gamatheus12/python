 # list_sum = 0
#
#for numeros in range (1,50):
#	list_sum = list_sum + numeros
#	print(list_sum)
#
#lista = [1,2,3,4,5,6,7,8,9,10]


print (" Trabalho de Fibonacci ")

n =int( input(" Digite Quantos termos você deseja :"))
t1 = 0
t2 = 1
t3 = 0

while t3 <= n:
    print("{}.".format(t3), end="")
    t3 = t1 + t2
    t1 = t2
    t2 = t3

print( " Fim ")