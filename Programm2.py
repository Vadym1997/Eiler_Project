def fibonachi_even(n):
    Fib_mass = [0, 1, 2] + [0] * (n-2)
    summ = 2
    for i in range(3, n+1):
        Fib_mass[i] = Fib_mass[i-1] + Fib_mass[i-2]
        if Fib_mass[i] > 4000000:
            break
        if Fib_mass[i] % 2 == 0:
            summ += Fib_mass[i]
    return summ


print(fibonachi_even(106))