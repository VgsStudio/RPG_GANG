import random

def dado20(x):
    n = random.randint(1,20)
    n += x
    return n


def dado10():
    n = random.randint(1,10)
    return n

def dado8():
    n = random.randint(1,8)
    return n

def dado6():
    n = random.randint(1,6)
    return n

def dado4():
    n = random.randint(1,4)
    return n    


def dados_generico(x):
    x = str(x)
    x = int(x.replace('d',''))
    n = random.randint(1,x)
    return n
