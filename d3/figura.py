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
   * Implementar clase Figura 
   * Implemantar clase Círculo
   * Implementar clase Rectángulo
   * Implementar clase Triángulo
   * Implementar operaciones lógicas entre figuras (>, <, >=, <=, ==, !=)
   * Implementar operaciones aritméticas entre figuras (+,-,*,/,**)
   * Implement operaciones aritméticas entre números y figuras

"""

