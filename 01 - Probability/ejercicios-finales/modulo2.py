def factorial(n):
    if (n == 0): return 1
    else: return n * factorial(n-1) 

def combinatory(n,k):
    return factorial(n)/(factorial(k) * factorial(n-k))

def my_binomial(k,n,p):
    return combinatory(n,k)*pow(p,k)*pow(1-p,n-k)

def ej1():
    print(my_binomial(k=3, n=12, p=0.5))

def ej2and3():
    acc_prob = 0
    for k in range(5+1):
        acc_prob += my_binomial(k, n=10, p=0.5)
    print(acc_prob)

ej1()
ej2and3() 