from time import sleep


def fibonacci_gen(max_val=float('inf')):
    n1 = 0
    yield n1
    n2 = 1
    yield n2
    while n1 + n2 <= max_val:
        n1, n2 = n2, n1 + n2
        yield n2


if __name__ == '__main__':
    fibo_gen = fibonacci_gen(500)
    for el in fibo_gen:
        print(el)
        sleep(0.5)
