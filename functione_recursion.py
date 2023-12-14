# 3 parte de functione recursive
# function
# le functione telephone le functione
# ou est le functione arrete de telephone le functione

# factorial desune ne c'est pas
# def factorial(n: int) -> int:
#     product = 1
#     for i in range(n):
#         product = factorial(n-1) * n
#     return product
# print(factorial(4))
# print(factorial(0))
# print(factorial(10))

# def fib_ser(n: int):
#     if n in [1, 2]:
#         return 1
#     elif n > 2:
#         return fib_ser(n=1) + fib_ser(n-2)
# print(fib_ser(20))

def fib_ser_vite(nth: int) -> int:
    last_n = 0
    n = 1
    sum = 1
    for i in range(nth-1):
        sum = n + last_n
        n, last_n = sum, n
    return sum
print(fib_ser_vite(10))