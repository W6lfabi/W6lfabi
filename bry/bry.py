from browser import document as D, html as H, ajax
from random import randrange as R 
D <= H.H1("Brython alap")
l  = list({R(1,10000) for i in range(200)})
l  . sort()
def f(e):
    e.target.innerHTML = ""
    e.target.style.backgroundColor = "green"
D <= H.DIV([H.DIV(i).bind("click", f) for i in l],Class="c")