# try:
#     numero=10
#     divisor=int(input("ingrese divisor: "))
#     pro= numero/divisor
# except ZeroDivisionError:
#     print("Error en la division")
# except ValueError:
#     print("Error cuando se paso el parametro")
# except Exception as e:
#     print("Error de tipo E, ocurrio el siguiente error:",e)
# else: 
#     print("Se ejecuta siempre que no se ejecuta el except")
# finally:
#     print("Se ejecuta siempre")

#Permite levantar o lanzar una exepcion, lo que se tipee luego del raise no lo cuenta
#raise ZeroDivisionError ("Lanzando una excepcion")

#assert
#comprueba una condicion y si es falsa lanza excepcion

#assert 1==2
#assert 1==2, "Errorsito con assertsito" #assert con mensaje

# Simil del raise con el assert
# print("Luego=================")
# if not 2==2:  # solo tomemos en cuenta la comparacion, si(True) no agarra , si (False) si agarra
#     raise NameError("Error similar al assert")
# print("Luego=================")

# def suma(a,b):
#     assert(type(a)==int)
#     assert(type(b)==int)
#     return a+b

# assert(suma(2,2)==5)



# CLASE EXCEPCION
# class Miexcepcion(Exception):
#     def __init__(self,param1,param2):
#         self.param1 = param1
#         self.param2 = param2
# try:
#     raise Miexcepcion({"param1":"valor param1","param2":"valor param2"}, "Info dgeneral de la excepcion")
# except Miexcepcion as ex:
#     print(ex.args[1])
#     info=ex.args[0]
#     print(info["param1"])
#     print(info["param2"])


def lee():
    intento=0
    while (intento<3):
        n=input("ingrese numero")
        try:
            n==int(n) # Si se puede realizar el casteo pasa a return y finaliza la funcion, sino va a except
            return n # puede ser break o quit()
        except ValueError:
            intento+=1
 
    raise(ValueError, "ingreso de valores incorrectos 3 veces, se accabo la chance")
    
lee()
# EN JERARQUIA , VALUE ERROR > ASSERT
def lee2(n):
    assert n==int(n),"Error en el parametro"

    
#lee2('2.5') # AQUI SALTARA EL ERROR DE VALUE_ERROR DEBIDO A Q NO PUEDE CASTEARLO SEA '2.5' O 'caracter'
#lee2(2.5) # AQUI TIENE UNA ENTRADA LA CUAL SI PUEDE CASTEAR A ENTERO, POR TANTO EVALUARA LA COMPARACION Y MOSTRARA EL ERROR DE ASSERT
#lee2('2') # AQUI TAMBIEN IENE UNA ENTRADA LA CUAL SI PUEDE CASTEAR A ENTERO Y MOSTRARA EL ERROR DE ASSERT
