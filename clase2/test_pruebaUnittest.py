import unittest 
    


def doblar(a): return a*2
def sumar(a,b): return a+b  
def es_par(a): return 1 if a%2 == 0 else 0
def cubo(a): return a * a * a

class PruebasFunciones(unittest.TestCase):

    def test_doblar(self):
        self.assertEqual(doblar(10), 20)
        self.assertEqual(doblar('Ab'), 'AbAb')

    def test_sumar(self):
        self.assertEqual(sumar(-15, 15), 0)
        self.assertEqual(sumar('Ab' ,'cd'), 'Abcd')

    def test_es_par(self):
        self.assertEqual(es_par(11), False)
        self.assertEqual(es_par(68), True)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['Hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)
    
    def test_cubo(self):
        self.assertEqual(cubo(10), 100)


if __name__ == '__main__':
    unittest.main()