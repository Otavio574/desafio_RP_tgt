def is_fibonnacci(num):
    if num < 0:
        return False
    
    fib_1, fib_2, = 0, 1

    if num == 0 or num == 1:
        return True
    
    while fib_2 < num:
        fib_1 = fib_2
        fib_2 = fib_1 + fib_2
    
    if fib_2 == num:
        return True

number = int(input())

if is_fibonnacci(number):
    print(f"O número {number} pertence à sequência de Fibonnacci")

else:
    print(f"O número {number} não pertence à sequência de Fibonnacci")