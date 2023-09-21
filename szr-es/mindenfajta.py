f = int(input("Forrás számrendszer (2 - 36): "))
c = int(input("Cél számrendszer (2 - 36): "))
kj = ["as", "es", "es", "as", "es", "ös", "os", "es", "as", "es"] * 5
kj[10], kj[40] = "es", "es"
az = " z   z" + " " * 40
szj = [chr(ord("0") + i) for i in range(10)] + [chr(i) for i in range(65, 91)]
szjo = {j: i for i, j in enumerate(szj)}
n = input(f"Átváltandó szám (csak a 0-{szj[f-1]} számjegyek): ")
ns = [i for i in n]
ns.reverse()
o, l, k = 0, [1], 1
for i, j in enumerate(ns):
    o += (f**i) * szjo[j]
print(f"A{az[szjo[ns[-1]]]} „{n}” ({f}-{kj[f]} számrendszerbeli) szám")
print(f"\t- tízes számrendszerbeli alakja: {o}")
if c != 10:
    while k <= o:
        k *= c
        l.append(k)
    l.pop()
    l.reverse()
    print(f"\t- {c}-{kj[c]} számrendszerbeli alakja: ", end="")
    for i in l:
        print(o // i, end="")
        o = o % i
    print()
