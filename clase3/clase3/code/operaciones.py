class Operaciones:
    """
    Esto es una clase llamada Operaciones que nos sirve de ejemplo
    
    * This is a bulleted list.
    * It has two items, the second
    item uses two lines.

    1. This is a numbered list.
    2. It has two items too.

    #. This is a numbered list.
    #. It has two items too.
    
    Atributos
    ---------
    op1:
        atributo uno de la clase
    op2:
        atributo dos de la clase
    
    Métodos
    -------
    suma:
        Realiza la suma de 2 números
    
    resta:
        Realiza la resta de 2 números
        
    >>>> resta(2,3)
    """
    
    def __init__(self,op1,op2):
        self.op1=op1
        self.op2=op2
        
    def suma(self):
        """Esta función realiza la suma
        """
        return self.op1+self.op2

    def resta(self):
        """Esta función realiza la resta
        """
        return self.op1-self.op2