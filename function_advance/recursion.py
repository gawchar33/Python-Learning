# factorial of number using the recursion
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))


#fibonacci series 
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
print(fibo(2))

