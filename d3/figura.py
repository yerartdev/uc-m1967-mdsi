# -*- coding: utf-8 -*-
"""Módulo para entregable UC M1967 OOPFormasGeometricas.

Todo:
    * Implementar Pruebas unitarias de operaciones lógicas (>=,<=,==,!=)
    * Implementar Pruebas unitarias de operaciones aritméticas (*,//,**)
    * Implementar Pruebas unitarias de operaciones entre números y figuras
    * Implementar pruebas unitarias de casos extremos ('corner test cases'): Circulo, Rectangulo, Triangulo
    * Documentar módulo, clases y métodos con Docstring

"""


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

    #::GMG::Operadores artirméticos entre objetos de la misma clase
    #       o entre un número entero positivo y un objeto
    # https://www.reddit.com/r/learnpython/comments/3cvgpi/can_someone_explain_radd_to_me_in_simple_terms_i/
    def __add__(self, other):
        if (isinstance(other, int) and other >= 0):
            res = Figura([x + other for x in self._magnitud])
        elif isinstance(other,self.__class__): 
            res = Figura([sum(x) for x in zip(self._magnitud,other._magnitud)])
        else:
            raise ValueError(
                '::ERROR::Sorry, {} is not a valid right operand'.format(other)
                )
        #::GMG::Cast the object returned to the actual class it belongs to
        # https://stackoverflow.com/questions/3464061/cast-base-class-to-derived-class-python-or-more-pythonic-way-of-extending-class
        res.__class__ = self.__class__
        return res

    # https://stackoverflow.com/questions/36785417/how-to-properly-overload-the-add-method
    def __radd__(self, other):
        return self.__add__(other)

    #- 	object.__sub__(self, other)
    def __sub__(self, other):
        if (isinstance(other, int) and other >= 0):
            res = Figura([x - other for x in self._magnitud])
        elif isinstance(other,self.__class__):
            res = Figura(
                tuple([x - y for x, y in zip(self._magnitud, other._magnitud)])
                )
        else:
            raise ValueError(
                '::ERROR::Sorry, {} is not a valid right operand'.format(other)
                )
        res.__class__ = self.__class__
        return res

    def __rsub__(self, other):
        return self.__sub__(other)

    #* 	object.__mul__(self, other)
    def __mul__(self,other):
        if (isinstance(other, int) and other >= 0):
            res = Figura([x*other for x in self._magnitud])
        elif isinstance(other,self.__class__):
            res = Figura(
                tuple([x*y for x, y in zip(self._magnitud, other._magnitud)])
                )
        else:
            raise ValueError(
                '::ERROR::Sorry, {} is not a valid right operand'.format(other)
            )
        res.__class__ = self.__class__
        return res

    def __rmul__(self, other):
        return self.__mul__(other)

    #// object.__floordiv__(self, other)
    def __floordiv__(self, other):
        if (isinstance(other, int) and other >= 0):
            res = Figura([x//other for x in self._magnitud])
        elif isinstance(other,self.__class__):
            res = Figura(
                tuple([x//y for x, y in zip(self._magnitud, other._magnitud)])
                )
        else:
            raise ValueError(
                '::ERROR::Sorry, {} is not a valid right operand'.format(other)
            )
        res.__class__ = self.__class__
        return res

    def __rfloordiv__(self, other):
        #return self.__floordiv__(other)
        raise RuntimeError("::ERROR:: Divide a {} by a {} doesn't make sense."
                .format(type(other),type(self))
            )

    #/ 	object.__truediv__(self, other)
    #::GMG::Notimplemented
    #       Considero que no tiene sentido porque trabajo con `longitudes` que son
    #       números enteros positivos

    #** .. pow() object.__rpow__(self, other)
    def __pow__(self,other):
        if (isinstance(other, int) and other >= 0):
            res = Figura([x**other for x in self._magnitud])
        elif isinstance(other,self.__class__):
            res = Figura(
                tuple([x**y for x, y in zip(self._magnitud, other._magnitud)])
            )
        else:
            raise ValueError(
                '::ERROR::Sorry, {} is not a valid right operand'.format(other)
            )
        res.__class__ = self.__class__
        return res

    def __rpow__(self, other):
        raise RuntimeError("::ERROR:: A {} raised to a {} doesn't make sense."
                .format(type(other),type(self))
            )

    #::GMG::Operadores lógicos 
    #< 		object.__lt__(self, other)
    def __lt__(self, other):
        if isinstance(other,self.__class__):
            return self.area() < other.area()
        else:
            raise ValueError(
                '::ERROR::Sorry, operands {} and {} not the same class'
                .format(self,other)
            )

    #<= 	object.__le__(self, other)
    def __le__(self, other):
        if isinstance(other,self.__class__):
            return self.area() <= other.area()
        else:
            raise ValueError(
                '::ERROR::Sorry, operands {} and {} not the same class'
                .format(self,other)
            )

    #== 	object.__eq__(self, other)
    def __eq__(self, other):
        if isinstance(other,self.__class__):
            return self.area() == other.area()
        else:
            raise ValueError(
                '::ERROR::Sorry, operands {} and {} not the same class'
                .format(self,other)
            )

    #!= 	object.__ne__(self, other)
    def __ne__(self, other):
        if isinstance(other,self.__class__):
            return self.area() != other.area()
        else:
            raise ValueError(
                '::ERROR::Sorry, operands {} and {} not the same class'
                .format(self,other)
            )

    #>= 	object.__ge__(self, other)
    def __ge__(self, other):
        if isinstance(other,self.__class__):
            return self.area() >= other.area()
        else:
            raise ValueError(
                '::ERROR::Sorry, operands {} and {} not the same class'
                .format(self,other)
            )

    #> 		object.__gt__(self, other)
    def __gt__(self, other):
        if isinstance(other,self.__class__):
            return self.area() > other.area()
        else:
            raise ValueError(
                '::ERROR::Sorry, operands {} and {} not the same class'
                .format(self,other)
            )


class Circulo(Figura):

    def __init__(self, radio=None):
        super().__init__((radio,))

    def radio(self):
        return self._magnitud[0]

    def perimetro(self):
        return 2*pi*self._magnitud[0]

    def area(self):
        return pi*(self._magnitud[0]**2)


class Rectangulo(Figura):

#    def __init__(self, lado_1=None, lado_2=None):
#        if (lado_1 and lado_2
#            and isinstance(lado_1, int) and isinstance(lado_2, int)
#            and lado_1 >= 0 and lado_2 >= 0:
#            super().__init__(tuple([lado_1,lado_2]))
#        else:
#            super().__init()

    def __init__(self, lado_1=None, lado_2=None):
        super().__init__(tuple([lado_1,lado_2]))

    def area(self):
        return self._magnitud[0]*self._magnitud[1]

    def longitud(self):
        return self._magnitud[0]

    def anchura(self):
        return self._magnitud[1]

from math import sqrt

class Triangulo(Figura):

#    def __init__(self, lado_1=None, lado_2=None, lado_3=None):
#        if (lado_1 and lado_2 and lado_3
#            and isinstance(lado_1, int) and isinstance(lado_2, int)
#            and isinstance(lado_3, int)
#            and lado_1 >= 0 and lado_2 >= 0 and lado_3 >= 0 and
#            _triangulo_valido(lado_1, lado_2, lado_3):
#            super().__init__(tuple([lado_1,lado_2,lado_3]))
#        else:
#            super().__init()

    def __init__(self, lado_1=None, lado_2=None, lado_3=None):
        if self._triangulo_valido(lado_1, lado_2, lado_3):
            super().__init__(tuple([lado_1,lado_2,lado_3]))
        else:
            super().__init()

    # https://en.wikipedia.org/wiki/Triangle_inequality
    # https://en.wikipedia.org/wiki/Triangle#Existence_of_a_triangle
#    @staticmethod
#    def _triangulo_valido(a, b, c):
#        if (a + b <= c) or (a + c <= b) or (b + c <= a) :
#            return False
#        else:
#            return True

    @staticmethod
    def _triangulo_valido(a, b, c):
        if a >= 0 and b >= 0  and c >= 0 and max(a,b,c) <= (a + b + c)/2:
            return True
        else:
            return False

    # https://en.wikipedia.org/wiki/Triangle#Computing_the_area_of_a_triangle
    def area(self):
        #s = (self._magnitud[0] + self._magnitud[1] + self._magnitud[2])/2
        s = self.perimetro()/2
        return sqrt(s*(s - self._magnitud[0])*\
                      (s - self._magnitud[1])*\
                      (s - self._magnitud[2]))


import unittest

class BaseTest(unittest.TestCase):

    a = Circulo(3)
    b = Circulo(7)
    c = Rectangulo(3,7)
    d = Rectangulo(1,3)
    e = Triangulo(3,4,5)
    f = Triangulo(2,2,3)

    def testCommon(self):
        print('::GMG::BaseTest:testCommon')

        print('::Circulo::->',self.a)
        print('::Circulo:área: {}, perímetro: {}'.\
             format(self.a.area(),self.a.perimetro()))
        # https://stackoverflow.com/questions/8929005/unittest-sometimes-fails-because-floating-point-imprecision#
        self.assertAlmostEqual(self.a.perimetro(), 2*pi*3,\
            msg='::ERROR:Circulo.perimetro():')
        self.assertAlmostEqual(self.a.area(), pi*3*3,\
            msg='::ERROR:Circulo.area():')

        print('::Rectangulo::->',self.c)
        print('::Rectangulo:área: {}, perímetro: {}'.\
             format(self.c.area(),self.c.perimetro()))
        self.assertEqual(self.c.perimetro(), 10,\
            msg='::ERROR:Rectangulo.perimetro():')
        self.assertEqual(self.c.area(), 21,\
            msg='::ERROR:Rectangulo.area():')

        print('::Triangulo::->',self.e)
        print('::Triangulo:área: {}, perímetro: {}'.\
             format(self.e.area(),self.e.perimetro()))
        self.assertEqual(self.e.perimetro(), 12,\
            msg='::ERROR:Triangulo.perimetro():')
        self.assertEqual(self.e.area(), 6.0,\
            msg='::ERROR:Triangulo.area():')


class SubTestAritmetico(BaseTest):

    def testSubSuma(self):
        print ('::GMG::SubTestAritmético::__add__::+')
        suma_c = self.a + self.b
        suma_r = self.c + self.d
        suma_t = self.e + self.f
        print('::Circulo:suma: {} + {} = {}'
            .format(self.a, self.b, suma_c))
        self.assertEqual(suma_c.radio(), 10)
        print('::Rectangulo:suma: {} + {} = {}'
            .format(self.c, self.d, suma_r))
        self.assertEqual(suma_r.longitud(), 4)
        self.assertEqual(suma_r.anchura(),10)
        print('::Triangulo:suma: {} + {} = {}'
            .format(self.e, self.f, suma_t))
        self.assertEqual(suma_t._magnitud, (5,6,8))

    def testSubResta(self):
        print('::GMG::SubTestAritmético::__sub__::-')
        resta_c = self.b - self.a
        resta_r = self.c - self.d
        resta_t = self.e - self.f
        print('::Circulo:resta: {} - {} = {}'
            .format(self.b, self.a, resta_c))
        self.assertEqual(resta_c.radio(), 4)
        print('::Rectangulo:resta: {} - {} = {}'
            .format(self.c, self.d, resta_r))
        self.assertEqual(resta_r.longitud(), 2)
        self.assertEqual(resta_r.anchura(),4)
        print('::Triangulo:resta: {} - {} = {}'
            .format(self.e, self.f, resta_t))
        self.assertEqual(resta_t._magnitud, (1,2,2))


class SubTestLogico(BaseTest):

    def testSubMayor(self):
        print('::GMG::SubTestLogico:">"')
        print('::Circulo: {} > {}'.format(self.b, self.a))
        print('::Circulo:área 1: {}, área 2: {}'.\
             format(self.b.area(),self.a.area()))
        self.assertEqual(self.b > self.a, True)

        print('::Rectangulo: {} > {}'.format(self.c, self.d))
        print('::Rectangulo:área 1: {}, área 2: {}'.\
             format(self.c.area(),self.d.area()))
        self.assertEqual(self.c > self.d, True)

        print('::Triangulo: {} > {}'.format(self.e, self.f))
        print('::Triangulo:área 1: {}, área 2: {}'.\
             format(self.e.area(),self.f.area()))
        self.assertEqual(self.e > self.f, True)

    def testSubMenor(self):
        print('::GMG::SubTestLogico:"<"')
        print('::Circulo: {} < {}'.format(self.a, self.b))
        print('::Circulo:área 1: {}, área 2: {}'.\
             format(self.a.area(),self.b.area()))
        self.assertEqual(self.a < self.b, True)

        print('::Rectangulo: {} < {}'.format(self.d, self.c))
        print('::Rectangulo:área 1: {}, área 2: {}'.\
             format(self.d.area(),self.c.area()))
        self.assertEqual(self.d < self.c, True)

        print('::Triangulo: {} < {}'.format(self.f, self.e))
        print('::Triangulo:área 1: {}, área 2: {}'.\
             format(self.f.area(),self.e.area()))
        self.assertEqual(self.f < self.e, True)


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    unittest.main()
