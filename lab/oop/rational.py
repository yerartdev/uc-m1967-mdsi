# -*- coding: utf-8 -*-
"""Implementation of a Rational class. 

This is a Master of Data Science M1967 class exercise. This module implements a Rational python class as laid out by a series of slides in a M1967 presentation introduction to Python OOP. This Docsting is formatted as stated in Napoleon's Example Google Style Python Docstrings.

.. _Example Google Style Python Docstrings:
   https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

Example:
   This module is intented to be used as an import only in a program or 
   interactive session::

      >> import rational as r
      >> a = r.Rational(3,5)
      >> b = r.Rational(7)
      >> print(a+b)
      (38/5)

Attributes:
   No module level variables.

Todo:
   * Implement Rational operations (op): +,-,*,/,**
   * Implement Integer op Rational and Rational op Integer

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""

class Rational:
  """A rational number object implementation with common binary operators.

  In mathematics, a rational number is any number that can be expressed as 
  the quotient or fraction p/q of two integers, a numerator p and a non-zero 
  denominator q. As defined in::

  .. _Rational number in Wikipedia:
     https://en.wikipedia.org/wiki/Rational_number

  Attributes:
    numerator   (:obj:`int`, optional): integer numerator of fraction.
      Defaults to None.
    denominator (:obj:`int`, optional): integer denominator of fraction.
      Defaults to None.

  """

  def __init__(self,num=None,den=None):
    """Initialisation of the rational or fraction.

    A rational o fraction may be created as a Not a Number, denoted by N/A.
    If no numerator is provided or if denominator is zero then rational is 
    N/A. Providing a non integer numerator or denominator is interpreted as
    not providing the attribute.

    If no denominator is provided then it is assumed to be 1. Since
    the denominator may be equal to 1, every integer is a rational number. 

    Note:
      Do not include the `self` parameter in the ``Args`` section.

    Args:
      num (:obj:`int`, optional): integer numerator.
      den (:obj:`int`, optional): integer denominator.

    """
    if isinstance(num,int):
      self.numerator = num
      if isinstance(den,int):
        if num < 0 and den < 0:
          self.numerator = abs(num)
          self.denominator = abs(den)
        elif num > 0 and den < 0:
          self.numerator = -1*num
          self.denominator = abs(den)
        else:
          self.denominator = den
      else:
        self.denominator = None
    else:
      self.numerator = None
      self.denominator = None

  def __str__(self):
    """String representation of a rational (fraction) number.

    The fraction is represented as ``numerator/denominator`` or ``N/A``.

    """
    if self.numerator == None or self.denominator == 0:
      return str('N/A')
    elif self.denominator == None or self.denominator == 1:
      return str(self.numerator) + '/1'
    else:
      return str(self.numerator) + "/" + str(self.denominator)

