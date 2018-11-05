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
  """The summary line for a class docstring should fit on one line.

  If the class has public attributes, they may be documented here
  in an ``Attributes`` section and follow the same formatting as a
  function's ``Args`` section. Alternatively, attributes may be documented
  inline with the attribute's declaration (see __init__ method below).

  Properties created with the ``@property`` decorator should be documented
  in the property's getter method.

  Attributes:
      attr1 (str): Description of `attr1`.
      attr2 (:obj:`int`, optional): Description of `attr2`.

  """

  def __init__(self,num=None,den=None):
    """Example of docstring on the __init__ method.

        The __init__ method may be documented in either the class level
        docstring, or as a docstring on the __init__ method itself.

        Either form is acceptable, but the two should not be mixed. Choose one
        convention to document the __init__ method and be consistent with it.

        Note:
            Do not include the `self` parameter in the ``Args`` section.

        Args:
            param1 (str): Description of `param1`.
            param2 (:obj:`int`, optional): Description of `param2`. Multiple
                lines are supported.
            param3 (:obj:`list` of :obj:`str`): Description of `param3`.

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
    """By default special members with docstrings are not included.

        Special members are any methods or attributes that start with and
        end with a double underscore. Any special member with a docstring
        will be included in the output, if
        ``napoleon_include_special_with_doc`` is set to True.

        This behavior can be enabled by changing the following setting in
        Sphinx's conf.py::

            napoleon_include_special_with_doc = True

    """
    if self.numerator == None or self.denominator == 0:
      return str('N/A')
    elif self.denominator == None or self.denominator == 1:
      return str(self.numerator) + '/1'
    else:
      return str(self.numerator) + "/" + str(self.denominator)

