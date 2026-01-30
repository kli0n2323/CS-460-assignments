from hw1_simple import add_strints, simple_recursive_multiplication
from hw1_karatsuba import karatsuba_multiplication
import time, statistics

def bench(fn, x, y, reps=200):
    times = []
    for _ in range(reps):
        t0 = time.perf_counter()
        fn(x, y)
        t1 = time.perf_counter()
        times.append(t1-t0)
    return statistics.median(times), statistics.mean(times)

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
        # 128 digits
        (
        "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679",
        "27182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274",
        )
    ]

    for x, y in tests:
        s_med, s_avg = bench(simple_recursive_multiplication, x, y)
        k_med, k_avg = bench(karatsuba_multiplication, x, y)
        speedup = s_med / k_med
        percent = (speedup - 1) * 100
        print(len(x), "digits",
              "| SIMPLE MEDIAN:", s_med,
              "| KARATSUBA MEDIAN:", k_med,
              "| SPEEDUP:", speedup,
              "| SPEEDUP PERCENT:", percent)

       