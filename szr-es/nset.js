class myMap extends Map {
    set(p, r) {
        if (this.has(p)) {
            var l = super.get(p)
            if (typeof l == 'number' && typeof r == 'number')
                super.set(p, (r + l) / 2)
            else super.set(p, l + r)
        } else super.set(p, r)
    }
}
s = new myMap()
s.set(3, 2)
s.set(4, 7)
s.set(4, 5)
s.set(3, "Cica")
s.set(1, "Kacsa")
console.log(s)