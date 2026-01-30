from hw1.hw1_simple import add_strints

def np_of_two(n: int) -> int:
    return 1 if n <= 1 else 1 << (n-1).bit_length()

def normalize(x: str, y: str) -> tuple[str, str]:
    # padding for var evenness
    if x == '':
        x = '0'
    if y == '':
        y = '0'

    n = max(len(x), len(y))
    n2 = np_of_two(n)

    return x.zfill(n2), y.zfill(n2)

def karatsuba_multiplication(x: str, y: str) -> str:
    x, y = normalize(x, y)

    # base case
    n = len(x)
    if n == 1:
        return str(int(x) * int(y))
    
    m = n // 2
    a = x[:m]
    b = x[m:]
    c = y[:m]
    d = y[m:]

    ac = karatsuba_multiplication(a, c)
    bd = karatsuba_multiplication(b, d)

    aplusb = add_strints(a, b)
    cplusd = add_strints(c, d)

    aplusb, cplusd = normalize(aplusb, cplusd)
    abcd = karatsuba_multiplication(aplusb, cplusd)

    abcd = karatsuba_multiplication(aplusb, cplusd)

    term0 = str(int(abcd) - int(ac) - int(bd))

    term1 = ac + ("0" * n)
    term2 = term0 + ("0" * m)

    return str(int(term1) + int(term2) + int(bd))
