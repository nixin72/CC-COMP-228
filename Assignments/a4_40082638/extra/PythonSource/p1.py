def pow(base, exp):
    powVal = 1

    if exp < 0:
        raise "Cannot have negative exponent"

    while exp != 0:
        powVal = mult(base, powVal)
        exp -= 1

    return powVal


def mult(p1, p2):
    multVal = 0

    if p1 == 0:
        return multVal

    while p2 != 0:
        if p2 < 0:
            multVal -= p1
            p2 += 1
        else:
            multVal += p1
            p2 -= 1

    return multVal

def main():
    x = -25
    y = 0
    if (x < 5):
        y = x - 2
        x = 20
    else:
        y = -1 * (x**3)
        x = 8

    print(x)
    print(y)

    return 0

main()
