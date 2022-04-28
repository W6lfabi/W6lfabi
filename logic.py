from browser import document as D, html as H
D <= H.H1("Táblázat")
def f(x):
    return 1 if x == 1 else x * f(x-1)
l = [
    [f"{i}<sup>2</sup>" for i in range(1, 10)],
    [f"{i ** 2}" for i in range(1, 10)],
    [""]*9,
    [f"{i}!" for i in range(1, 10)],
    [f"{f(i)}" for i in range(1, 10)]
]
D <= H.TABLE(H.TR(H.TD(e) for e in r) for r in l)