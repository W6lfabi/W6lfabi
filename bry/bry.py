from browser import document as D, html as H, ajax
D <= H.H1("Brython alap")
def f(x):
    l = x.text.split("\n")
    for r in l:
        u = r.split(";")
        D <= H.SPAN(u[1]) + ": " + H.SPAN(u[0]) + H.HR()
def g(e):
    D <= H.DIV(e.target.value)
    e.target.value = ""
D <= H.INPUT().bind("change", g) + H.HR()
ajax.get("teszt.txt", oncomplete = f)