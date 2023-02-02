from pimath.number.fraction import Fraction
class Unknown(object):
    count=0
    def __init__(self,name=None,uuid=None):
        if uuid is None:
            self.uuid=Unknown.count
            Unknown.count+=1
        else:
            self.uuid=uuid
        self.name=name
    def __repr__(self):
        if self.name is None:
            return 'X{}'.format(self.uuid)
        else:
            return self.name

class IntExp(object):
    # ((系数,(未知数1,次数),(未知数2,次数)...),...)
    def __init__(self,monos=()):
        self.monos=monos
    def __neg__(self):
        def neg_mono(mono):
            res=(-mono[0],)+mono[1:]
            return res
        monos=self.monos
        neg_monos=tuple(map(neg_mono,monos))
        return IntExp(neg_monos)
    def __add__(self,other):
        monos=self.monos
        other_monos=other.monos
        return IntExp(monos+other_monos)
    def __sub__(self,other):
        monos=self.monos
        other_monos=(-other).monos
        return IntExp(monos+other_monos)
    def __mul__(self,other):
        def reduction_mono(mono):
            mono_dict={}
            for u in mono[1:]:
                if u[0] in mono_dict.keys():
                    mono_dict[u[0]]+=u[1]
                else:
                    mono_dict[u[0]]=u[1]
            res=(mono[0],)
            for u in mono_dict.keys():
                res+=((u,mono_dict[u]),)
            return res

        def mul_mono(mono1,mono2):
            res=(mono1[0]*mono2[0],)+mono1[1:]+mono2[1:]
            return reduction_mono(res)  
        
        monos=self.monos
        other_monos=other.monos
        res=()
        for m in monos:
            for n in other_monos:
                res+=(mul_mono(m,n),)
        return IntExp(res)
    def __floordiv__(self,num):
        return IntExp(((Fraction(1)/num,),))*self
    def __repr__(self):
        def repr_mono(mono):
            text=repr(mono[0])
            for u in mono[1:]:
                text+=' * '
                text+=repr(u[0])
                text+=' ** '
                text+=repr(u[1])
            return text
        text=''
        for mono in self.monos:
            text+=repr_mono(mono)
            text+=' + '
        text=text[:-3]
        return text
    def reduction(self):
        def reduction_mono(mono):
            mono_dict={}
            for u in mono[1:]:
                if u[0] in mono_dict.keys():
                    mono_dict[u[0]]+=u[1]
                else:
                    mono_dict[u[0]]=u[1]
            n_mono_dict=sorted(mono_dict.items(),key=lambda d:d[0].uuid)
            res=(mono[0],)
            for u in n_mono_dict:
                res+=(u,)
            return res
        
        monos=self.monos
        monos=tuple(map(reduction_mono,monos))
        mono_dict={}
        for m in monos:
            if m[1:] in mono_dict.keys():
                mono_dict[m[1:]]+=m[0]
            else:
                mono_dict[m[1:]]=m[0]
        res=()
        for m in mono_dict.keys():
            if mono_dict[m]!=0:
                res+=((mono_dict[m],)+(m),)
        return IntExp(res)
    @classmethod
    def simple(cls,num):
        if type(num) == Unknown:
            return IntExp(((Fraction(1),(num,Fraction(1))),))
        else:
            return IntExp(((Fraction(num),),))

class Equation(object):
    def __init__(self,exp1,exp2):
        self.exp1=exp1
        self.exp2=exp2
    def solve_eq_1_1(self):
        exp=self.exp1-self.exp2
        exp=exp.reduction()
        exp=exp.monos
        const=0
        unknown=0
        x=0

        if len(exp)==1:
            if len(exp[0])==1:
                const=exp[0][0]
            else:
                unknown=exp[0][0]
        elif len(exp)==2:
            if len(exp[0])==1:
                const=exp[0][0]
                unknown=exp[1][0]
            else:
                const=exp[1][0]
                unknown=exp[0][0]
        else:
            raise TypeError
        
        if unknown == 0:
            if const== 0:
                return 'All'
            else:
                return None
        else:
            return -const/unknown
