"""Bucles for sobre listas con valores básicos."""

# TODO A partir de esta lista de números enteros muestra solo los pares.
numbers: list[int] = [7, 8, 11, 14, 15, 2, 10, 3]

for num in numbers:
    if(num % 2 == 0):
        print(num)

# TODO Muestra por pantalla la suma de los números impares de la lista
# `numbers`.
added: int = 0

for num in numbers:
    if(num % 2 != 0):
        added += num
        
print(added)

# TODO Muestra por pantalla qué suma da un resultado menor: la suma de los
# números pares o la suma de los números impares. Deberás mostrar un mensaje
# como este (me lo invento):
#
# "La suma de los números pares da un resultado menor: 35"
added_peers: int = 0
added_odds: int = 0

for num in numbers:
    if(num % 2 == 0):
        added_peers += num
    elif(num % 2 != 0):
        added_odds += num

if(added_odds > added_peers):
    print(f"La suma de los números pares me ha dado un numero menor: {added_peers}")
elif(added_peers > added_odds):
    print(f"La suma de los números mpares me ha dado un numero menor: {added_odds}")

# TODO Muestra por pantalla cuántos números pares e impares hay.
counter_pairs: int = 0
counter_odds: int = 0

for num in numbers:
    if(num % 2 == 0):
        counter_pairs += 1
    elif(num % 2 != 0):
        counter_odds += 1
        
print(f"Hay un total de {counter_pairs} números pares y {counter_odds} números de impares")