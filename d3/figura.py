# -*- coding: utf-8 -*-
"""Módulo para entregable UC M1967 OOPFormasGeometricas.

Entregable UC Master of Data Science M1967. Este módulo implementa una
jerarquía de clases basada en el conceptos: figura geométrica, círculo,
rectángulo y triángulo. Sigue las instrucciones indicadas por el equipo
docente.

Entrega:

.. _.py con la implementación de las clase (este módulo)
.. _.ipynb (y .html) con ejemplos de uso y comentarios.

Instrucciones:

Realizar un módulo en Python aplicando programación orientada a objetos referido a formas Geométricas. En este caso se creará al menos una clase por cada forma geométrica básica: Círculo, Rectángulo y Triángulo. Todas ellas deberán de heredar de una clase "Figura", que definirá los métodos básicos a implementar por cada una de las formas formas geométricas.

También deberéis experimentar con la sobrecarga de operadores en Python. Sobrecargar __repr__ y __str__ (ver el link), para que muestre la información de la forma geométrica.

Con respecto a los operadores aritméticos (+, -, *, /, **), al operar 2 figuras se operará con los parámetros de la forma geométrica. Esto significa que si sumamos 2 círculos, se creará un nuevo círculo son su radio sumado. Si suma un objeto de tipo numérico, entonces se le aplicará a cada uno de los atributos de la figura.

Con respecto a los operadores lógicos se usará el área de la forma para comparar las figuras. Esto permitirá comparar distintos tipos de figura, y por tanto podrá implementarse los comparadores en la clase "Figura".

Ejemplo:
    Sesión interactiva ipython::

        >> import figura as f
        >> a = f.Rectangulo(3,5)
        >> b = f.Rectangulo(2,7)
        >> c = 3
        >> print('Compara Rectángulos',a, 'y',b,': a > b -> ',a > b)
        Compara rectángulos R(3,5) y R(2,7) : a > b -> True
        True
        >> print('Suma Rectángulos',a, 'y',b,': a + b -> ',a + b)
        Suma rectángulos R(3,5) y R(2,7) : a + b -> R(5,12)
        >> print('Suma entero y rectángulo',a, 'y',c,': a + c -> ',a + c)
        Suma entero y rectángulo R(3,5) y 3 : a + c -> R(6,8)

Attributes:
    No hay variables de módulo.

Todo:
    * Documentar __str__, num_lados, perimetro, area
    * Implementar Pruebas unitarias de clase Figura
    * Implemantar clase Circulo
    * Implementar clase Rectangulo
    * Implementar clase Triangulo
    * Implementar Pruebas unitarias de clases: Circulo, Rectangulo, Triangulo
    * Implementar operaciones lógicas entre figuras (>, <, >=, <=, ==, !=)
    * Implementar Pruebas unitarias de operaciones lógicas
    * Implementar operaciones aritméticas entre figuras (+,-,*,/,**)
    * Implementar Pruebas unitarias de operaciones aritméticas
    * Implement operaciones aritméticas entre números y figuras
    * Implementar Pruebas unitarias de operaciones entre números y figuras
    * Implementar Pruebas unitarias en Notebook Python para entregable

"""


pi = 3.14159265359
"""float: relación entre la longitud de una circunferencia y su diámetro en geometría euclidiana.

Para más información::

.. _Wikipedia: Número π:
    https://es.wikipedia.org/wiki/N%C3%BAmero_%CF%80

"""


class Figura(object):
    """Clase que representa una figura geométrica.

    Attributes:
        _lados (int): número de lados de la figura geométrica.
        magnitud (:obj:`tuple`, opcional): secuencia de números enteros positivos inmutable
        que representa la ``longitud`` de cada lado.

    """
    
    _nombre = 'Figura'

    def __init__(self, mag=None):
        #::GMG::Solamente una secuencia de números enteros positivos válida
        if (mag and isinstance(mag, (list, tuple)) and \
            all(x >= 0 for x in mag)):
            self.magnitud = tuple(mag)
            self._lados = len(mag)
        else:
            self.magnitud = tuple()
            self._lados = 0

    def __str__(self):
        if self.magnitud:
            return str(self._nombre) + str(list(self.magnitud))
        else:
            return str(self._nombre) +  str('(NaF)') #::GMG::NaF = Not a Figure

    def num_lados(self):
        return self._lados

    def perimetro(self):
        s = 0
        for i in self.magnitud:
            s+=i
        return s

    def area(self):
        pass


class Circulo(Figura):
    pass


class Rectangulo(Figura):
    pass


class Triangulo(Figura):
    pass


"""Parte de las pruebas de Figura, Circulo, Rectangulo, Triangulo.

"""

def test_rectangulo():
    a = Rectangulo(3,5)
    #b = Rectangulo(2,7)

    area_real = 15
    perimetro_real = 8
    area = a.area()
    perimetro_1 = a.perimetro()
    perimetro_2 = Figura.primetro(a)
    assert area == area_real, \
        '::GMG::test_rectangulo()::a.area()::Error, area esperada=%s, calculada=%s ' \
        % (area_real,area)

#import unittest

#class BaseTest(unittest.TestCase):
#    def testCommon(self):
#        print 'Calling BaseTest:testCommon'
#        value = 5
#        self.assertEquals(value, 5)

#class SubTest1(BaseTest):
#    def testSub1(self):
#        print 'Calling SubTest1:testSub1'
#        sub = 3
#        self.assertEquals(sub, 3)


#class SubTest2(BaseTest):
#    def testSub2(self):
#        print 'Calling SubTest2:testSub2'
#        sub = 4
#        self.assertEquals(sub, 4)

#if __name__ == '__main__':
#    unittest.main()