from collections import namedtuple
import pytest


Task = namedtuple('Task', ['resumen', 'propietario', 'finalizado', 'id'])
# parametros por default cuando no se invocan
Task.__new__.__defaults__ = ( None, None, False, None )
 
def test_defaults():
   #Al no utilizar parametros, se invoca al método por default 
   t1 = Task()
   t2 = Task(None, None, False, None)
   assert t1 == t2
 
 
def test_corroborar():
   #Valida la generación de atributos de namedtuple 
   t = Task('Gastos del mes', 'Juan')
   assert t.resumen == 'Gastos del mes'
   assert t.propietario == 'Juan'
   assert (t.finalizado, t.id) == (False, None)

def test_diccionario():
   #El método _asdict() devuelve un diccionario. 
   t_task = Task('Ingresos mensuales', 'Pedro', True, 21 )
   t_dict = t_task._asdict()
   esperado = {'resumen': 'do something',
               'propietario': 'Pedro',
               'finalizado': True,
               'Id': 21}
   assert t_dict == esperado
 
 
def test_replace():
   #replace() cambia el valor de los atributos
   t_antes = Task('documentacion hecha', 'Juan', False)
   t_despues = t_antes._replace(id=10, finalizad=True)
   t_esperado = Task('documentacion hecha', 'Juan', True, 10)
   assert t_despues == t_esperado

def test_suma():
    x=-4
    y=4
    posx=abs(x)
    assert y==posx