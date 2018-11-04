class Rational:
  numerator = None
  denominator = None
  
  def __init__(self,num=None,den=None):
    if isinstance(num,int):
      self.numerator = num
      if isinstance(den,int):
        self.denominator = den
        if num < 0 and den < 0:
          self.numerator = abs(num)
          self.denominator = abs(den)
        elif num > 0 and den < 0:
          self.numerator = -1*num
          self.denominator = abs(den)

  def __str__(self):
    if self.numerator == None or self.denominator == 0:
      return str('N/A')
    elif self.denominator == None or self.denominator == 1:
      return str(self.numerator) + '/1'
    else:
      return str(self.numerator) + "/" + str(self.denominator)

