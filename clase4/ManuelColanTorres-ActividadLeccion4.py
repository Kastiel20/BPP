import pdb
pdb.set_trace()

lista= [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

# lista comprimida
maximos= [max(x) for x in lista]
print(maximos)


nl= [3, 4, 8, 5, 5, 22, 13]


# funcion calcular primos
def es_primo(n):
    for i in range(2,n):
        if  n%i == 0:
            return False
    return n

# Filter para obtener lista de primos       
primos = list(filter(es_primo, nl))
print(primos)