*cs, x = list(map(int, input().split(',')))

def p(_cs):
    def f(_x):
        s = 0
        xn = 1

        for _c in _cs:
            s += _c * xn
            xn *= _x

        return s
    return f

print(p(cs)(x))