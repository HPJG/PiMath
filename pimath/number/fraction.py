from pimath.function.classic import gcd

class Fraction(object):
    def __init__(self,numerator=0,denominator=1):
        if type(numerator) == Fraction:
            self.numerator=numerator.numerator
            self.denominator=numerator.denominator
        else:
            self.numerator=numerator
            self.denominator=denominator
    def num(self):
        # 返回分子
        return self.numerator
    def den(self):
        # 返回分母
        return self.denominator
    def __neg__(self):
        num=-self.num()
        den=self.den()
        return Fraction(num,den)
    def __add__(self,other):
        other=Fraction(other)
        num=self.num()*other.den()+other.num()*self.den()
        den=self.den()*other.den()
        return Fraction(num,den)
    def __sub__(self,other):
        other=Fraction(other)
        num=self.num()*other.den()-other.num()*self.den()
        den=self.den()*other.den()
        return Fraction(num,den)
    def __mul__(self,other):
        other=Fraction(other)
        num=self.num()*other.num()
        den=self.den()*other.den()
        return Fraction(num,den)
    def __truediv__(self,other):
        other=Fraction(other)
        num=self.num()*other.den()
        den=self.den()*other.num()
        return Fraction(num,den)
    def __eq__(self,other):
        other=Fraction(other)
        return self.num()*other.den()==self.den()*other.num()
    def __gt__(self,other):
        other=Fraction(other)
        return self.num()*other.den()>self.den()*other.num()
    def __lt__(self,other):
        other=Fraction(other)
        return self.num()*other.den()<self.den()*other.num()
    def __repr__(self):
        return '{}/{}'.format(self.num(),self.den())
    def reduction(self):
        num=self.num()
        den=self.den()
        while num!=int(num) or den!=int(den):
            num*=10
            den*=10
        num=int(num)
        den=int(den)
        gcd_value=gcd(num,den)
        num=num//gcd_value
        den=den//gcd_value
        return Fraction(num,den)
    def __int__(self):
        return self.num()//self.den()
    def __float__(self):
        return self.num()/self.den()
    def __hash__(self):
        return hash(self.numerator/self.denominator)