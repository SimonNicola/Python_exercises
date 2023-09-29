"""Bucles y tuplas."""

# TODO A continuación tienes una lista de tuplas con los nombres y las edades
# de los perros de una competición canina.
#
# Escribe un programa que muestre por pantalla el nombre y la edad del perro
# más joven y el perro mayor.
dogs: list[tuple[str, int]] = [
    ("Otto", 7), ("Oriol", 8), ("Chess", 3), ("Capitán", 5), ("Juani", 5)
]
oldest_name: str 
oldest_age: int = 0
youngest_name: str
youngest_age: int = dogs[0][1]


for name,age in dogs:
    if(age > oldest_age):
        oldest_age = age
        oldest_name = name
    elif(age < youngest_age):
        youngest_age = age
        youngest_name = name
        
print(f"Perro más joven es {youngest_name} con una edad de {youngest_age}")

print(f"Perro más viejo es {oldest_name} con una edad de {oldest_age}")