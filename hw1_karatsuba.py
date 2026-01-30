from hw1_simple import add_strints

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

    abcd = karatsuba_multiplication(aplusb, cplusd)

    term0 = str(int(abcd) - int(ac) - int(bd))

    term1 = ac + ("0" * n)
    term2 = term0 + ("0" * m)

    return str(int(term1) + int(term2) + int(bd))

# sanity check
if __name__ == "__main__":
    tests = [
        ("12", "34"),
        ("99", "99"),
        ("0123", "0456"),
        ("1234", "5678"),
        ("0000", "0000"),
        ("1111", "0001"),
        ("1234567890123456", "9876543210123456"),
        ("12345678901234561234567890123456", "12345678901234561234567890123456"),
        ("1234567890123456123456789012345612345678901234561234567890123456", "1234567890123456123456789012345612345678901234561234567890123456"),
    ]

    for x, y in tests:
        # Compare against Python int multiplication for correctness.
        got = karatsuba_multiplication(x, y)
        want = str(int(x) * int(y))
        print(f"{x} * {y} = {got}  (ok={got == want})")