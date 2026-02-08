# gap penalty
a_gap = 1

# misalignment penalty
def A(x, y):
    if x == y:
        return 0
    return 1

# compute minimum alignment scores
def NEEDLEMAN_WUNCH(X, Y): 
    # len of input strings
    m = len(X)
    n = len(Y)

    # init penalty table P (m rows, n columns)
    P = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # init base cases: P(0, 0), P(i, 0), P(0, j)
    for i in range (1, m + 1):
        P[i][0] = i * a_gap
    for j in range(1, n + 1):
        P[0][j] = j * a_gap
    
    # fill in the rest of the table, offest by 1 bc first character of a string is
    # at [0] but first row/col of P is for empty string base case
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            P[i][j] = min(
                P[i - 1][j - 1] + A(X[i-1], Y[j-1]),
                P[i - 1][j] + a_gap,
                P[i][j - 1] + a_gap,
            )
    return P

def fancy_print(P):
    for i in range(len(P)):
        for j in range(len(P[0])):
            print(f"{P[i][j]:5d} ", end="")
        print()


def traceback(X, Y):
    P = NEEDLEMAN_WUNCH(X, Y)
    x_aligned = []
    y_aligned = []
    i = len(X)
    j = len(Y)



    while (i, j) != (0, 0):

        curr = P[i][j]

        if i == 0:
            x_aligned.append('-')
            y_aligned.append(Y[j - 1])

            j -= 1
            continue

        if j == 0:
            x_aligned.append(X[i - 1])
            y_aligned.append('-')

            i -= 1
            continue

        a = A(X[i - 1], Y[j - 1])
        diagonal = P[i - 1][j - 1] + a 
        up = P[i - 1][j] + a_gap
        left = P[i][j - 1] + a_gap

        if (curr == diagonal) and (X[i - 1] == Y[j - 1]):
            x_aligned.append(X[i - 1])
            y_aligned.append(Y[j - 1])

            i -= 1
            j -= 1
            continue
        if curr == left:
            x_aligned.append('-')
            y_aligned.append(Y[j - 1])

            j -= 1
            continue
        if curr == up:
            x_aligned.append(X[i - 1])
            y_aligned.append('-')

            i -= 1
            continue

        if (curr == diagonal):
            x_aligned.append(X[i - 1])
            y_aligned.append(Y[j - 1])

            i -= 1
            j -= 1
            continue

    
    true_x = ''.join(reversed(x_aligned))
    true_y = ''.join(reversed(y_aligned))

    print(true_x)
    print(true_y)
    print('')


# RUN PROGRAM

tests = [
    ["CRANE", "RAIN"],
    ["CYCLE", "BICYCLE"],
    ["ASTRONOMY", "GASTRONOMY"],
    ["INTENTION", "EXECUTION"],
    ["AGGTAB", "GXTXAYB"],
    ["GATTACA", "GCATGCU"],
    ["DELICIOUS", "RELIGIOUS"],
]

for pair in tests:
    X = pair[0]
    Y = pair[1]

    P = NEEDLEMAN_WUNCH(X, Y)
    #fancy_print(P)
    alignment = traceback(X, Y)
