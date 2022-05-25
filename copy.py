def Karatsuba(x, y):
    m = (len(str(x)) // 2)
    a = x // 10 ** m
    b = x % 10 ** m
    c = y // 10 ** m
    d = y % 10 ** m

    if len(str(x)) == 1:
        return x * y
    else:
        a_c = Karatsuba(a, c)
        b_d = Karatsuba(b, d)
        ad_bc = Karatsuba(a + b, c + d) - a_c - b_d
        res = 10 ** (2 * m) * a_c + 10 ** m * ad_bc + b_d
        return res
print(Karatsuba(63413453435435463,4645465466464))