#Função para que consiga buscar o número por extenso
def number_to_portuguese(n):
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["", "dez", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    especiais = ["", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    centenas = ["", "cem", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seicentos", "setecentos", "oitocentos", "novecentos"]

    if n == 1000:
        return "mil"
    elif 100 < n < 1000:
        return centenas[n // 100] + (" e " + number_to_portuguese(n % 100) if n % 100 != 0 else "")
    elif n < 100:
        if n < 10:
            return unidades[n]
        elif 10 < n < 20:
            return especiais[n - 10]
        else:
            return dezenas[n // 10] + (" e " + unidades[n % 10] if n % 10 != 0 else "")
    else:
        return "Número fora do intervalo suportado"

#Função que pegue o primeiro número acima de 19 que, por extenso, comece com D
def next_number_starting_with_d(start):
    num = start + 1
    while True:
        word = number_to_portuguese(num)
        if word.startswith("d"):
            return num
        num += 1

#Sequência de ímpares
def next_element_a(seq):
    return seq[-1] + 2

#Sequências de potências de 2
def next_element_b(seq):
    return seq[-1] * 2

#Sequências de quadrados
def next_element_c(seq):
    next_index = len(seq)
    return next_index ** 2

#Quadrados apenas de números pares
def next_element_d(seq):
    next_index = (len(seq) + 2) * 2  
    return next_index ** 2

#Sequência de Fibonnacci
def next_element_e(seq):
    return seq[-1] + seq[-2]

#Busca pelo primeiro número que se inicia com 'D' após o Dezenove.
def next_element_f(seq):
    return next_number_starting_with_d(seq[-1])

# Testando as funções
print("a) Próximo elemento:", next_element_a([1, 3, 5, 7]))       # 9
print("b) Próximo elemento:", next_element_b([2, 4, 8, 16, 32, 64])) # 128
print("c) Próximo elemento:", next_element_c([0, 1, 4, 9, 16, 25, 36])) # 49
print("d) Próximo elemento:", next_element_d([4, 16, 36, 64]))   # 100
print("e) Próximo elemento:", next_element_e([1, 1, 2, 3, 5, 8]))  # 13
print("f) Próximo elemento:", next_element_f([2, 10, 12, 16, 17, 18, 19])) # 20
