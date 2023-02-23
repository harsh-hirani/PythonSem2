# Display the user specified term in Fibonacci series using a recursive function fibo()
def fibo(n):
    if n<2:
        return 1
    return (fibo(n-1)+fibo(n-2))
value = int(input('Enter the term of Fibonacci series: '))
print('nth term of Fibonacci series: ',fibo(value))