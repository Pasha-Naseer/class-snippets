# Collection Data Type
# tuple
# ordered, unchangeable, allows duplicates
cities = ("Milan", "Rome", "Florence", "Catania", "Venice")
print(cities)

print(cities[1])
print(cities[2:4])

# methods
print(cities.count("Rome"))
print(cities.index("Venice"))

# dict
# ordered, changeable, no duplicated keys
authors_and_books = {"Camus": "The outsider",
                     'Cervantes': "Don Quixote",
                     'Bulgakov': "The Master and Margarita",
                     }
print(authors_and_books)

print(authors_and_books['Camus'])

authors_and_books.pop('Camus')
print(authors_and_books)

authors_and_books.popitem()
print(authors_and_books)

print(authors_and_books.get('Cervantes'))  # No Error if it doesn't exist
print(authors_and_books["Cervantes"])  # Error is case the key is absent

authors_and_books['Shakespeare'] = "King Lear"
print(authors_and_books)

# see now I'll call the new list books_and_authors which is different
books = ["the wealth of nations", "the theory of moral sentiments", "the invisible hand"]
books_and_authors = dict.fromkeys(books, "Adam Smith")
print(books_and_authors)

print(authors_and_books.keys())
print(authors_and_books.values())
print(authors_and_books.items())

authors_and_books.setdefault('Immanuel Kant', "critique of pure reason")
print(authors_and_books)

authors_and_books.update({'Edgar Allan Poe': "the raven", 'Charles Dickens': "Bleak House"})
print(authors_and_books)
