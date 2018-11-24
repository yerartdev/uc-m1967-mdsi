pi = 3.14159265359

class Figura(object):

    def __init__(self, mag=None):
        #::GMG::Solamente una secuencia de números enteros positivos válida
        if (mag and isinstance(mag, (list, tuple)) and \
            all((isinstance(x, int) and x >= 0) for x in mag)):
            self._magnitud = tuple(mag)
        else:
            self._magnitud = tuple()

    def __repr__(self):
        if self._magnitud:
            return str(self.__class__.__name__) + \
		str(list(self._magnitud))
            #return '{}{}'.format(self.__class__.__name__, self.magnitud)
        else:
            return str(self.__class__.__name__) +  str('[NaF]') #::GMG::NaF = Not a Figure
            #return '{}(NaF)'.format(self.__class__.__name__) 

    def num_lados(self):
        return len(self._magnitud)

    def perimetro(self):
        return sum(self._magnitud)

    #::GMG::NotImplemented (left for inheritance)
    #       Las operaciones de comparación asociadas al área se dejan también para las clases hijas
    def area(self):
        pass

    #::GMG::Las funciones aritméticas se pueden implementar sabiendo self.magnitud
    # https://www.reddit.com/r/learnpython/comments/3cvgpi/can_someone_explain_radd_to_me_in_simple_terms_i/
    def __add__(self, other):
        res = Figura([sum(x) for x in zip(self._magnitud,other._magnitud)])
        #::GMG::Cast the object reurned to the actual class it belongs to
        # https://stackoverflow.com/questions/3464061/cast-base-class-to-derived-class-python-or-more-pythonic-way-of-extending-class
        res.__class__ = self.__class__
        return res

    #- 	object.__sub__(self, other)
    def __sub__(self, other):
        res = Figura(tuple([x-y for x, y in zip(self._magnitud, other._magnitud)]))
        res.__class__ = self.__class__
        return res

    #* 	object.__mul__(self, other)
    def __mul__(self,other):
        res =  Figura(tuple([x*y for x, y in zip(self._magnitud, other._magnitud)]))
        res.__class__ = self.__class__
        return res

    #// object.__floordiv__(self, other)
    def __floordiv__(self, other):
        res = Figura(tuple([x//y for x, y in zip(self._magnitud, other._magnitud)]))
        res.__class__ = self.__class__
        return res

    #/ 	object.__truediv__(self, other)
    #::GMG::Notimplemented
    #       Considero que no tiene sentido porque trabajo con `longitudes` que son
    #       números enteros positivos

    #** .. pow() object.__rpow__(self, other)
    def __pow__(self,other):
        res = Figura(tuple([x**y for x, y in zip(self._magnitud, other._magnitud)]))
        res.__class__ = self.__class__
        return res

class Circulo(Figura):

    def __init__(self, radio=None):
        super().__init__((radio,))

    def radio(self):
        return int(self._magnitud[0])

    def perimetro(self):
        return 2*pi*self._magnitud[0]

    def area(self):
        return pi*(self._magnitud[0]**2)

    #< 		object.__lt__(self, other)
    def __lt__(self, other):
        return self.area() < other.area()

    #<= 	object.__le__(self, other)
#    def __le__(self, other):
#        return self.area() <= other.area()

    #== 	object.__eq__(self, other)
#    def __eq__(self, other):
#        return self.area() == other.area()

    #!= 	object.__ne__(self, other)
#    def __ne__(self, other):
#        return self.area() != other.area()

    #>= 	object.__ge__(self, other)
#    def __ge__(self, other):
#        return self.area() >= other.area()

    #> 		object.__gt__(self, other)
    def __gt__(self, other):
        return self.area() > other.area()


#class Rectangulo(Figura):
#    _nombre = 'Rectangulo'

#    def __init__(self, lado_1=None, lado_2=None):
#        if (lado_1 and lado_2
#            and isinstance(lado_1, int) and isinstance(lado_2, int)
#            and lado_1 >= 0 and lado_2 >= 0:
#            super().__init__(tuple([lado_1,lado_2]))
#        else:
#            super().__init()

    #https://stackoverflow.com/questions/805066/call-a-parent-classs-method-from-child-class-in-python
#    def perimetro(self):
#        pass
    #    return sum(self.magnitud)

#    def area(self):
#        pass


    #< 		object.__lt__(self, other)
    #<= 	object.__le__(self, other)
    #== 	object.__eq__(self, other)
    #!= 	object.__ne__(self, other)
    #>= 	object.__ge__(self, other)
    #> 		object.__gt__(self, other)


#class Triangulo(Figura):
#    _nombre = 'Triangulo'

#    def __init__(self, lado_1=None, lado_2=None, lado_3=None):
#        if (lado_1 and lado_2 and lado_3
#            and isinstance(lado_1, int) and isinstance(lado_2, int)
#            and isinstance(lado_3, int)
#            and lado_1 >= 0 and lado_2 >= 0 and lado_3 >= 0 and
#            _triangulo_valido(lado_1, lado_2, lado_3):
#            super().__init__(tuple([lado_1,lado_2,lado_3]))
#        else:
#            super().__init()

#    @staticmethod
#    def _tiangulo_valido(a, b, c):
        # check condition
#        if (a + b <= c) or (a + c <= b) or (b + c <= a) :
#            return False
#        else:
#            return True

#    def perimetro(self):
#        return sum(self.magnitud)

#    def area(self):
#        pass


    #< 		object.__lt__(self, other)
    #<= 	object.__le__(self, other)
    #== 	object.__eq__(self, other)
    #!= 	object.__ne__(self, other)
    #>= 	object.__ge__(self, other)
    #> 		object.__gt__(self, other)


import unittest

class BaseTest(unittest.TestCase):

    a = Circulo(3)

    def testCommon(self):
        print ('::GMG::BaseTest:testCommon')
        print('::GMG::Circulo::->',self.a)
        perimetro = self.a.perimetro()
        area = self.a.area()
        print('::GMG::Circulo:área: {}, perímetro: {}'.\
             format(area,perimetro))
        # https://stackoverflow.com/questions/8929005/unittest-sometimes-fails-because-floating-point-imprecision#
        self.assertAlmostEqual(perimetro, 2*pi*3,\
            msg='::GMG::ERROR:Circulo.perimetro():')
        self.assertAlmostEqual(area, pi*3*3,\
            msg='::GMG::ERROR:Circulo.area():')

class SubTestAritmetico(BaseTest):

    b = Circulo(7)

    def testSubSuma(self):
        print ('::GMG::SubTestAritmético:testSubSuma')
        suma = self.a + self.b
        #::GMG::
        #suma.__class__ =  Circulo
        print('::GMG::Circulo:suma: {} + {}'.format(self.a, self.b))
        self.assertEqual(suma.radio(), 10)

class SubTestLogico(BaseTest):

    b = Circulo(5)

    def testSubMayor(self):
        print ('::GMG::SubTestLogico:">"')
        print('::GMG::Circulo: {} > {}'.format(self.b, self.a))
        self.assertEqual(self.b > self.a, True)

# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    unittest.main()
