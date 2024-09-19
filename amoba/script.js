
var t = []
window.onload = f = () => {
    m = window.innerWidth > 1000 ? 20 : 7
    nyert = "-"
    t = Array(10).fill(0).map(() => Array(m).fill(0))
    let t1 = document.getElementById("t1")
    t1.innerHTML = `<table id="table">${
        t   .map((v, i) =>`<tr>
                ${v .map((_, j) =>
                        `<td onclick="katt(${i},${j})" id="${i}-${j}"></td>`)
                    .join("")}</tr>`)
            .join("")
    }
    </table>`
}
var [next, nyert] = "O-"
katt = (i, j) => {
    cell = document.getElementById(i + "-" + j)
    if (cell.innerHTML == "" && nyert=="-") {
        cell.innerHTML = next
        t[i][j] = next;
        [[1, 1], [1, 0], [1, -1], [0, 1]].forEach(([a, b]) => {
            [x, y, k] = [i, j, 0]
            while (t[x] && t[x][y] == next) k++, x += a, y += b;
            [x, y] = [i, j]
            while (t[x] && t[x][y] == next) k++, x -= a, y -= b
            if (k >= 6) nyert = next
        })
        next = next == "O" ? "X" : "O";
        cell.classList.add(next)
    }
    document.getElementById("nyert").innerHTML = nyert != "-" ? `
    <div onclick="f()" class="nyert">${nyert} nyert, új játszma</div>
    ` : ``
}
