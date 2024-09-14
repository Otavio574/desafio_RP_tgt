def is_there_a (word):
    count = 0

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