def add_strints(x: str, y: str) -> str:
    """
    Add two nonnegative integer strings by converting to int.
    This method can be rewritten as a sum/carry adder for a
    single digit addition, pulling characters from the
    input strings. For simplicity now, we just convert the
    whole string to integer, do the addition, and then
    convert the number back to string.
    """
    return str(int(x) + int(y))

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

def simple_recursive_multiplication(x: str, y: str) -> str:
    """
    Recursive multiplication for nonnegative integer strings.
    Assumptions:
      - len(x) == len(y)
      - len(x) is a power of two
      - x and y contain only digits
    Uses:
      xy = ac*10^n + (ad+bc)*10^(n/2) + bd
    """
    x, y = normalize(x, y)

    # Number of digits in x, y
    n = len(x)
    # Base case
    if n == 1:
        return str(int(x) * int(y))
    # Middle of x, y for splitting them in left/right halves
    m = n // 2
    # Divide x, y into left/right halves
    a = x[:m]
    b = x[m:]
    c = y[:m]
    d = y[m:]
    # Compute the partial solution
    ac = simple_recursive_multiplication(a, c)
    ad = simple_recursive_multiplication(a, d)
    bc = simple_recursive_multiplication(b, c)
    bd = simple_recursive_multiplication(b, d)
    # Conquer the partial solutions
    ad_plus_bc = add_strints(ad, bc)
    # Multiply by powers of 10 via appending zeros (string shift).
    term1 = ac + ("0" * n)
    term2 = ad_plus_bc + ("0" * m)
    # Final sum (Using int conversion for addition to keep things simple)
    return str(int(term1) + int(term2) + int(bd))