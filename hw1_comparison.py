from hw1_simple import add_strints, simple_recursive_multiplication
from hw1_karatsuba import karatsuba_multiplication
import time

# SANITY CHECK --

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
        want = str(int(x) * int(y))

        s_start = time.time()
        s_got = simple_recursive_multiplication(x, y)
        s_end = time.time()
        s_duration = s_end - s_start
        print("[ SIMPLE: ] " + f"{x} * {y} = {s_got}  (ok={s_got == want})" + f" TIME: {s_duration}")

        k_start = time.time()
        k_got = karatsuba_multiplication(x, y)
        k_end = time.time()
        k_duration = k_end - k_start
        print("[ KARATSUBA: ] " + f"{x} * {y} = {k_got}  (ok={k_got == want})" + f" TIME: {k_duration}")
        print('')