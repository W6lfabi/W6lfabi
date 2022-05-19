from browser import document as D, html as H
from random import shuffle
for i in range(6):
    l = list(range(1, 91))
    shuffle(l)
    l = l[:5]
    l.sort()
    D <= [
        H.DIV(e, Class=f"c{i % 3}" ) for i, e in enumerate(l)
    ]
    D <= H.HR()
