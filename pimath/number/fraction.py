from pimath.function.classic import gcd

class Fraction(object):
    def __init__(self,numerator=0,denominator=1):
        self.numerator=numerator
        self.denominator=denominator
    def num(self):
        # 返回分子
        return self.numerator
    def den(self):
        # 返回分母
        return self.denominator
    def __add__(self,other):
        num=self.num()*other.den()+other.num()*self.den()
        den=self.den()*other.den()
        return Fraction(num,den)
    def __sub__(self,other):
        num=self.num()*other.den()-other.num()*self.den()
        den=self.den()*other.den()
        return Fraction(num,den)
    def __mul__(self,other):
        num=self.num()*other.num()
        den=self.den()*other.den()
        return Fraction(num,den)
    def __truediv__(self,other):
        num=self.num()*other.den()
        den=self.den()*other.num()
        return Fraction(num,den)
    def __eq__(self,other):
        return self.num()*other.den()==self.den()*other.num()
    def __gt__(self,other):
        return self.num()*other.den()>self.den()*other.num()
    def __lt__(self,other):
        return self.num()*other.den()<self.den()*other.num()
    def __repr__(self):
        return '{}/{}'.format(self.num(),self.den())
    def reduction(self):
        num=self.num()//gcd(self.num(),self.den())
        den=self.den()//gcd(self.num(),self.den())
        return Fraction(num,den)
