# OOP
# Object-Oriented Programming
class Book:
    # class variable
    is_published = True

    # constructor
    # initializer
    def __init__(self, name, writer, pub_date, subject):  # parameterized constructor
        self.name = name
        self.writer = writer
        self.pub_date = pub_date
        self.subject = subject

    # custom method
    def critique(self, writer, text):
        return f"{writer} wrote an essay on the {self.name}:\n\"{text}\""

    def __str__(self):
        return f"{self.name} - {self.writer}"


# instance
book1 = Book("The Outsider", "Albert Camus", 1942, "Literature & philosophy")
book2 = Book("Don Quixote", "Miguel de Servantes", 1605, "spanish Literature")
print(book1)
print(book2)
print(book1.critique("Jean-Paul Sartre", "Good Good Good very goood"))

user = str(input("Enter Your name: "))
essay = str(input("Write Down Your Essay: "))
print(book2.critique(user, essay))


# Inheritance
class PoemBook(Book):
    def __init__(self, name, writer, pub_date, subject, language):
        super().__init__(name, writer, pub_date, subject)
        self.language = language

    def structure(self, structure):
        return f"{self.name} is a {structure}"

    def critique(self, writer, text):
        pass

    # str
    def __str__(self):
        return f"{self.name} - {self.writer} - {self.subject}"


poem_book1 = PoemBook("Divaneh Hafez", "Hafez-e-Shirazi", "1813 H.Gh", "Love and drinking", "Persian")
print(poem_book1)

print(poem_book1.critique("Hushang Ebtehaj", "Good Good BVery Goood"))


# make an objects
class Person:
    # class variable
    has_lungs = True

    # built-in constructor
    # initializer
    def __init__(self, name, last_name, age):  # Parameterized constructor not default constructor
        self.name = name  # object variable
        self.last_name = last_name
        self.age = age

    # custom method
    def run(self, direction):
        sentence = f"{self.name} Running {direction}"
        return sentence

    # string representation
    def __str__(self):
        return self.name


# instance
ali = Person("Ali", "Shokuhi", 17)
print(ali)

hosna = Person("Hosna", "Rezvani", 23)
print(hosna)

print(ali.run("forward"))

print(ali.age)

print(ali.has_lungs)
print(hosna.has_lungs)


# Single Inheritance
class Programmer(Person):
    def __init__(self, name, last_name, age, coding_language, ide):
        super().__init__(name, last_name, age)
        self.coding_language = coding_language
        self.ide = ide

    # custom method
    def working_on(self, project_name):
        return f"{self.name} is working on {project_name} project..."

    # if we don't write run() method again it will use Paren class Run()
    def run(self, direction):
        return "Ali can't run... reason --> unknown"

    # same with __str__
    def __str__(self):
        return f"{self.name} - {self.coding_language}"


ali = Programmer("Ali", "Shokoohi", 17, "Assembly/C/Rust/Python", "cmd")
print(ali)

print(ali.run("left"))


# multiple inheritance
class Horse:
    def __init__(self, breed):
        self.breed = breed

    def __str__(self):
        return self.breed


class Centaur(Person, Horse):
    def __init__(self, name, last_name, age, breed, god):
        super().__init__(name, last_name, age)
        Horse.__init__(self, breed)
        self.god = god

    def __str__(self):
        return f"{self.name} - {self.god}"


print(Centaur("Chiron", "The Greek", 125, "Greek", "Zeus"))
