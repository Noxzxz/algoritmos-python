import math, random
def NumReal(a):
    a = int(a)
    return(a)

def CalcHipot(a,b):
    c =(a*a + b*b)**(1/2)
    return(c)

def CalcAnglCos(a):
    a = math.radians(a)
    a = math.cos(a)
    return(a)

def CalcAnglSen(a):
    a = math.radians(a)
    a = math.sin(a)
    return(a)

def CalcAnglTang(a):
    a = math.radians(a)
    a = math.tan(a)
    return(a)

def SortAluno():
    a = random.randint(0,3)
    return a
    