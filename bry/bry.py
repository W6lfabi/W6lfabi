from browser import document, html
document <= html.H1("Hatványozás")
for i in range(1,30):
    document <= html.DIV(
        html.SPAN(i) +
        " négyzete: " +
        html.SPAN(i ** 2)
    )
    print(i, i ** 2)