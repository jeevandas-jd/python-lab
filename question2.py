
def read():
    x, y, z = input("enter three sides of triangle \n >>>").split()
    x, y, z = int(x), int(y), int(z)
    return x, y, z


def area(i, j, k):
    s = (i + j + k) / 2
    area = ((s * (s - i) * (s - j) * (s - k))**0.5)
    return area


def comparision(p, q):
    total = p + q
    pp, qp = (p / total) * 100, (q / total) * 100

    print(
        f"percentage contribution of first triangle = {round(pp)}% \nand percentage contribution of second triangle = {round(qp)}%")
    return pp, qp


a1, b1, c1 = read()
area1 = area(a1, b1, c1)

a2, b2, c2 = read()
area2 = area(a2, b2, c2)

comparision(area1, area2)