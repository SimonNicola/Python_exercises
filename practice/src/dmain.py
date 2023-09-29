"""Transformación de strings."""

# TODO Escribe un programa que pida un texto por pantalla y lo transforme de
# manera que aparezcan las consonantes primero y las vocales después.
#

text : str = input("Dime un texto")
vowels: list[str] = ["A", "E", "I", "O", "U"]
text = text.replace(" ", "")
text_list : list[str] = []
text_list_vowels : list[str] = []

for char in text:
    if char.upper() not in vowels:
        text_list.append(char)
    elif char.upper() in vowels:
        text_list_vowels.append(char)

text = text_list + text_list_vowels
        
result : str = "".join(text)

print(result) 
# Por ejemplo: si el usuario escribe el texto "Hola Amigo", el programa
# mostrará "HlmgoaAio".
#
# Como ves, aparecen las consonantes en el orden en que están en el texto y,
# después, las vocales en el orden en que están en el texto. Además, se
# respetan minúsculas y mayúsculas y los espacios desaparecen.
