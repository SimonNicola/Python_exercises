"""Bucles while"""

# TODO Escribe un programa que pida números al usuario por pantalla con input
# y construya una lista con los números pares y otra con los números impares.
# El programa dejará de pedir números cuando el usuario escriba el 0.
#
# Escribe este programa usando un bucle while.

peers: list [int] = []
odds: list [int] = []
number: int = 2

while(number != 0):
    
    number = int(input("Dime un numero"))    
        
    if(number % 2 == 0 and number != 0):
        peers.append(number)
    elif(number % 2 != 0 and number != 0):
        odds.append(number)
        
print(peers)
print(odds)