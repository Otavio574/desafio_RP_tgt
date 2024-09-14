#Receber input sobre o estado dos interruptores e das lâmpadas
def input_boolean(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['y', 'n']:
            if user_input == 'y':
                return True
            else:
                return False
        else:
            print("Entrada inválida. Por favor, insira 'Y' ou 'N'.")

def verificar_sala_1(a, b, c):
    b = False #Desligamento de B após um período
    if a == True and b == False and c == False: #Garantia de que A está ligado e B e C desligados
        aceso = input_boolean("A lâmpada está acesa?[Y/N] ")
        if not aceso:
            quente = input_boolean("A lâmpada está quente?[Y/N] ")

        if aceso == True:
            return 'A'
        elif quente == True:
            return 'B'
        else:
            return 'C'

def verificar_sala_2 (sala1, a, b):
    a = False
    b = False
    if sala1 == 'A':
        b = True
    else:
        a = True
    
    aceso = input_boolean("Aa lâmpada está acesa?[Y/N] ")
    
    if a == True:
        if aceso == True:
            return 'A'
        else:
            if sala1 == 'B':
                return 'C'
            else:
                return 'B'
   
    if b == True:
        if aceso == True:
            return 'B'
        else:
            return 'C'

def verificar_sala_3 (sala1, sala2):
    if sala1 == 'A':
        if sala2 == 'B':
            return 'C'
        else:
            return 'B'
    elif sala1 == 'B':
        if sala2 == 'A':
            return 'C'
        else:
            return 'A'
    else:
        if sala2 == 'A':
            return 'B'
        else:
            return 'A'


#Estado inicial dos interruptores, em que A e B estão ligados, enquanto C está desligado
a, b, c = True, True, False

resultado1 = verificar_sala_1(a, b)
print(f"Interruptor que controla a sala 1: {resultado1}")

resultado2 = verificar_sala_2(resultado1, a, b)
print(f"Interruptor que controla a sala 2: {resultado2}")

resultado3 = verificar_sala_3(resultado1, resultado2)
print(f"Interruptor que controla a sala 3: {resultado3}")

'''
Explicação da lógica:

Temos 3 interruptores, A B e C, em que A e B estão inicialmente ligados (portanto, com valor True) e C desligado (valor False)
Ao verificar a primeira sala, após desligarmos o interruptor B, verificaremos 2 parâmetros: o estado de aceso e o estado de estar quente, parâmetros booleanos
o pseudocódigo seria, para a sala 1:

Se Luz está acesa:
    A liga a sala 1
Caso não:
    Se a lâmpada está quente:
        B a liga (pois esquentou)
    Caso não:
        C a liga (não interferiu em nada)

Com isso, teremos apenas duas salas para verificar qual delas cada interruptor abre. basta então ligar um dos restantes.
Se, ao verificar a sala 2, notamos que a que ligamos ficou acesa, significa que essa acende a sala 2. Caso contrário, ela acende a sala 3
O pseudocódigo, então, seria, para a sala 2:

Se luz está acesa:
    interruptor escolhido liga a sala 2
Caso não:
    interruptor escolhido liga a sala 3

Com isso, o interruptor restante ligará a sala restante.

''' 