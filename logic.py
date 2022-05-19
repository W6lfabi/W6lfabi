from browser import document as D, html as H
from random import shuffle, randrange as R
s = [1,1,1,1,0,2,3,2,0,1,1,1,1]
def f(e):
    e.target.text = int(e.target.text) + 1
    e.target.style = {
        "boxShadow": "1px 1px 6px black",
        "backgroundColor": f"rgb({R(0,256)},{R(0,256)},{R(0,256)})"
    }
for i in range(12):
    l = list(range(1, 91))
    shuffle(l)
    l = l[:13]
    l.sort()
    D <= [
        H.DIV(e, Class=f"c{s[i]}").bind("click", f)
        for i, e in enumerate(l)
    ]
    D <= H.HR()
