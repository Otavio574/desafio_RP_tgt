
def is_there_a (word):
    #Contador de quantas vezes o A está na string
    count = 0

    #Função de percorrer a lista em busca do A, ao mesmo tempo que conta sempre que ele apaece
    for char in word:
        if char == 'a' or char == 'A':
            count += 1
        
    if count > 0:
        return True, count

    return False, count

text = input()

exists, count = is_there_a(text)

if exists:
    if count > 1:
        print(f"A letra 'a' aparece {count} vezes na string.")
    else:
        print(f"A letra 'a' aparece 1 vez na string.")
else:
    print ("A letra 'a' não aparece na string.")