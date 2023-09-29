"""Strings y listas de strings."""

# TODO Escribe un programa que indique cuántos espacios tiene un texto que
# tendrás que pedir por pantalla.

text: str = input("Dime un texto")
counter: int = 0

for char in text:
    if(char == " "):
        counter += 1

print(counter)

# TODO Escribe un programa que pida un texto y lo muestre por pantalla en
# minúsculas y sin espacios.

text_two: str = input("Segundo texto")

text_two = text_two.lower()

text_two = text_two.replace(" ", "")

print(text_two)

# TODO Escribe un programa que pida dos textos por pantalla e indique qué texto
# tiene más vocales (sin distinción entre mayúsculas y minúsculas).

text_three: str = input("tercer texto")
text_four: str = input("Cuarto texto")
vowels: list[str] = ["a","e","i","o","u"]
count: int = 0
count2: int = 0

for char in text_three:
    if char.lower() in vowels:
        count += 1
        
for char in text_four:
    if char.lower() in vowels:
        count2 += 1
        
if(count > count2):
    print(f"El tercer texto tiene más vocales con un total de {count}")
elif(count2 > count):
    print(f"El cuatro texto tiene más vocales con un total de {count2}")
elif(count == count2):
    print(f"Tienen las mismas vocales {count} texto tres, {count2} texto 2")
else:
    print("Error")