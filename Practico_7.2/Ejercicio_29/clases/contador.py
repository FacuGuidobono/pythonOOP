'''
+--------------------------------------------------------------------------------+
|                                                                                |
|                                                                                |
|                            CLASE CONTADOR MODULO                               |
|                                                                                |
|                                                                                |
+--------------------------------------------------------------------------------+


'''





class ContadorModulo:
    def __init__(self, modulo):
        self.modulo = modulo
        self.valor = 0

    @property
    def next(self):
        return self.__next__

    def __iter__(self):
        return self

    def __next__(self):
        if self.valor >= self.modulo:
            self.valor = 0
        resultado = self.valor
        self.valor += 1
        return resultado