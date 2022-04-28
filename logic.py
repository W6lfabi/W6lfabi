from browser import document as D, html as H
D <= H.H1("Abszolút értékek")
def f(x):
    return x if x > 0 else -x 
l = [
    [f"{i}" for i in range(-5, 6)],
    [f"{f(i)}" for i in range(-5, 6)]
]
D <= H.TABLE(H.TR(H.TD(e) for e in r) for r in l)