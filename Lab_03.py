# Створюємо глосарій
glossary = {
    "Python": "Мова програмування високого рівня, що має простий синтаксис та є зручною для початківців.",
    "Function": "Іменований блок коду, який виконує певну задачу і може бути викликаний у програмі.",
    "Variable": "Місцева комірка пам’яті для зберігання даних, які можуть змінюватися під час виконання програми.",
    "Loop": "Конструкція, що дозволяє виконувати блок коду багаторазово, поки виконується певна умова.",
    "Dictionary": "Неупорядкована структура даних у Python, яка зберігає пари ключ-значення."
}

# Виведення у спеціально відформатованому вигляді
for term, definition in glossary.items():
    print(f"{term}:\n\t{definition}\n")
# Створюємо словник з річками і регіонами
rivers = {
    "Amazon": "South America",
    "Nile": "Africa",
    "Danube": "Europe"
}

# Виведення повідомлень для кожної пари "річка: регіон"
for river, region in rivers.items():
    print(f"The {river} runs through {region}.")

# Створюємо словник з річками і регіонами
rivers = {
    "Amazon": "South America",
    "Nile": "Africa",
    "Danube": "Europe"
}

# Виведення повідомлень для кожної пари "річка: регіон"
for river, region in rivers.items():
    print(f"The {river} runs through {region}.")
# Створюємо англо-німецький словник
e2g = {
    "stork": "storch",
    "hawk": "falke",
    "woodpecker": "specht",
    "owl": "eule"
}

# Додаємо ще два слова у словник
e2g["sparrow"] = "spatz"
e2g["eagle"] = "adler"

# Виведення німецького варіанту слова "owl"
print("German translation for 'owl':", e2g["owl"])

# Виведення словника
print("\nFull dictionary:", e2g)

# Виведення ключів словника
print("\nKeys:", list(e2g.keys()))

# Виведення значень словника
print("Values:", list(e2g.values()))
# Створюємо словники для домашніх тварин
buddy = {"type": "dog", "owner": "Alex"}
whiskers = {"type": "cat", "owner": "Emily"}
nibbles = {"type": "rabbit", "owner": "Liam"}
goldy = {"type": "fish", "owner": "Sophia"}

# Зберігаємо словники в список pets
pets = [buddy, whiskers, nibbles, goldy]

# Виведення повідомлень
for pet in pets:
    print(f"{pet['owner']} is the owner of a pet - a {pet['type']}.")
# Словник азбуки Морзе
morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

# Отримання введення від користувача
letter = input("Enter a letter or digit: ").strip().upper()  # Приводимо до верхнього регістру

# Перевірка і виведення результату
if letter in morse:
    print(f"The Morse code for '{letter}' is: {morse[letter]}")
else:
    print("The character is not in the Morse code dictionary.")
# Створюємо багаторівневий словник
subjects = {
    "science": {
        "physics": ["nuclear physics", "optics", "thermodynamics"],
        "computer science": {},
        "biology": {}
    },
    "humanities": {},
    "public": {}
}

# Виведення ключів subjects['science']
print("Keys in subjects['science']:", list(subjects["science"].keys()))

# Виведення значень subjects['science']['physics']
print("Values in subjects['science']['physics']:", subjects["science"]["physics"])
# Створюємо словник cities
cities = {
    "Kyiv": {
        "country": "Ukraine",
        "population": "2.9 million",
        "fact": "Kyiv is one of the oldest cities in Eastern Europe, founded in the 5th century."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "14 million",
        "fact": "Tokyo is home to the busiest pedestrian crossing in the world - Shibuya Crossing."
    },
    "Paris": {
        "country": "France",
        "population": "2.1 million",
        "fact": "Paris is known as the 'City of Light' and is famous for the Eiffel Tower."
    }
}

# Виведення інформації про кожне місто
for city, info in cities.items():
    print(f"\nCity: {city}")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}")
# Створюємо словник команд NBA
teams = {
    "New York Knicks": [22, 7, 6, 9, 45],
    "Los Angeles Lakers": [25, 15, 3, 7, 55],
    "Chicago Bulls": [20, 12, 4, 4, 50],
    "Golden State Warriors": [23, 14, 2, 7, 52],
    "Boston Celtics": [24, 16, 1, 7, 54]
}

# Виведення даних у форматі
for team, stats in teams.items():
    print(f"{team.upper()} {' '.join(map(str, stats))}")
# Словник з речами гравця
things = {
    'key': 3,
    'mace': 1,
    'stone': 24,
    'lantern': 1,
    'gold coin': 10
}

# Виведення списку речей і підрахунок загальної кількості
print("Equipment:")
total_items = 0

for item, quantity in things.items():
    print(f"{quantity} {item}")
    total_items += quantity

# Виведення загальної кількості речей
print(f"Total number of things: {total_items}")
input("\nНатисніть Enter, щоб завершити програму...")
