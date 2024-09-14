#Lógica de Fibonnaacci
def is_fibonnacci(num):
    #A sequência só admite números naturais
    if num < 0:
        return False
    
    #Dois primeiros números da sequência
    fib_1, fib_2, = 0, 1

    #Garantindo os dois primeiros
    if num == 0 or num == 1:
        return True
    
    while fib_2 < num:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    
    #Se o número descrito em algum momento for igual ao último número da soma, é de fibonacci. Caso fique acima, significa que não pertence.
    if fib_2 == num:
        print('a')
        return True

    return False

number = int(input())

if is_fibonnacci(number):
    print(f"O número {number} pertence à sequência de Fibonnacci")

else:
    print(f"O número {number} não pertence à sequência de Fibonnacci")