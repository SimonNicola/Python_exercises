"""Tuplas y bucles."""

# TODO Escribe un programa que pida tres libros y los guarde en una lista.
#
# Cada libro constará de un título (str), un autor (str) y un número de páginas
# que serán guardados en tuplas, es decir, cada libro será una tupla y cada
# una de estas tuplas se guardará en una lista.
#
# Al final del programa, tendremos algo así (los datos son inventados):
# [
#     ("El mejor título para un libro", "María Martínez", 250),
#     ("Mar y montaña", "Rosario García", 180),
#     ("Playa y cordilleras", "Juan Tolomé", 375)
# ]


books : list[tuple[str, str, int]] = [
    
]

for num in range(3):
    title: str = input("Dime el nombre titulo del libro")
    author: str = input("Dime el autor del libro")
    pag: int = int(input("Dime el numero de páginas"))

    tuple: list[str] = (title,author,pag)

    books.append(tuple)


print(books)