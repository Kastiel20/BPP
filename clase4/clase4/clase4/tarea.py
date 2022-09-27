# import pdb
# pdb.set_trace()

lista= [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
maximos= [max(x) for x in lista]
#print(maximos)


nl= [3, 4, 8, 5, 5, 22, 13]

#funcion primo

#primosgosu = [  [  n  for i in range(2,n)  if n%i==0 ]   for n in nl   ] #primosgosu = [  [  [ n ]   for i in range(2,n)  if n%i==0 ]   for n in nl   ]
#print(primosgosu)

def es_primo(n):
    for i in range(2,n):
        if  n%i == 0:
            return False
    return n
             
primos = list(filter(es_primo, nl))
print(primos)



#940639825

# enteros = [2,3,4,5,6]

# fun_cuad = lambda x : x**2
# cuadrados = list(map(fun_cuad, enteros))
# print(cuadrados)

