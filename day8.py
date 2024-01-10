import math

def is_fib(n):
    expr1 = 5 * n**2 + 4
    expr2 = 5 * n**2 - 4
    return math.isqrt(expr1)**2 == expr1 or math.isqrt(expr2)**2 == expr2

print(is_fib(8))  
print(is_fib(15)) 
