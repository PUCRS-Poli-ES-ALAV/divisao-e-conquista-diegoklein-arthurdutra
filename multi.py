import random
import time
import math

cont = 0

def multi(x, y, n):
    global cont

    if n == 1:
        return x*y
    else:
        m = (n//2)
        a = (x//math.pow(2,m))
        b = (x%math.pow(2, m))
        c = (y//math.pow(2, m))
        d = (y%math.pow(2, m))
        e = multi(a, c, m)
        cont+=1
        f = multi(b, d, m)
        cont+=1
        g = multi(b, c, m)
        cont+=1
        h = multi(a, d, m)
        cont+=1
        return (math.pow(2, 2 * m) * e + (math.pow(2, 2 * m) * (g + h) + f))


## Não compreendemos como executar testes para este algoritmo. Apenas implemntamos o algoritmo pedido pelo professor.