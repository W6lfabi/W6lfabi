from browser import document as D, html as H
from random import randrange as R
r = [i for i in range(1,60)]
def f(x):
    return R(1, 60)
r.sort(key = f)
l = r[:20]
l.sort()
D <= H.DIV([H.DIV(f"{i} : {j}") for i,j in enumerate(l)], Class = "c")
