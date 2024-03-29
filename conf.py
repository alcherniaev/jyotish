grahas = {
    "Солнце": 190,
    "Луна": 213,
    "Меркурий": 345,
    "Венера": 177,
    "Марс": 118,
    "Юпитер": 275,
    "Сатурн": 20
}

exaltation = {
    "Солнце": 10,
    "Луна": 3,
    "Меркурий": 28,
    "Венера": 15,
    "Марс": 5,
    "Юпитер": 27,
    "Сатурн": 20
}

rashi_values = {
    "Овен": 0,
    "Телец": 1,
    "Близнецы": 2,
    "Рак": 3,
    "Лев": 4,
    "Дева": 5,
    "Весы": 6,
    "Скорпион": 7,
    "Стрелец": 8,
    "Козерог": 9,
    "Водолей": 10,
    "Рыбы": 11
}

saptavarga_bala_01 = {
    "МТ": 45,
    "О": 30,
    "БД": 20,
    "Д": 15,
    "Н": 10,
    "В": 4,
    "БВ": 2,
}

grahas_rashi = {
    "Солнце": ["Лев"],
    "Луна": ["Рак"],
    "Меркурий": ["Близнецы","Дева"],
    "Венера": ["Весы", "Телец"],
    "Марс": ["Овен", "Скорпион"],
    "Юпитер": ["Стрелец", "Рыбы"],
    "Сатурн": ["Водолей", "Козерог"],
    "Раху": ["Водолей"],
    "Кету": ["Овен"]
}


graha_perm_rel = {
    "Солнце": {
        'Друг': ['Луна', 'Марс', 'Юпитер'],
        'Нейтрал': ['Меркурий'],
        'Враг': ['Венера', 'Сатурн']
        },
    "Луна": {
        'Друг': ['Солнце', 'Меркурий'], 
        'Нейтрал': ['Венера', 'Марс', 'Юпитер', 'Сатурн'], 
        'Враг': None
        },
    "Марс": {
        'Друг': ['Луна', 'Солнце', 'Юпитер'], 
        'Нейтрал': ['Венера', 'Сатурн'], 
        'Враг': ['Меркурий']
        },
    "Меркурий": {
        'Друг': ['Солнце', 'Венера'], 
        'Нейтрал': ['Марс', 'Юпитер', 'Сатурн'], 
        'Враг': ['Луна']
        },
    "Юпитер": {
        'Друг': ['Луна', 'Марс', 'Солнце'], 
        'Нейтрал': ['Сатурн'], 
        'Враг': ['Венера', 'Меркурий']
        },
    "Венера": {
        'Друг': ['Меркурий', 'Сатурн'], 
        'Нейтрал': ['Юпитер', 'Марс'], 
        'Враг': ['Луна', 'Солнце']
        },
    "Сатурн": {
        'Друг': ['Меркурий', 'Венера'], 
        'Нейтрал': ['Юпитер'], 
        'Враг': ['Луна', 'Марс', 'Солнце']
        }
}

graha_direction = {
    "Овен": "Север",
    "Телец": "Север",
    "Близнецы": "Север",
    "Рак": "ЮГ",
    "Лев": "ЮГ",
    "Дева": "ЮГ",
    "Весы": "ЮГ",
    "Скорпион": "ЮГ",
    "Стрелец": "ЮГ",
    "Козерог": "Север",
    "Водолей": "Север",
    "Рыбы": "Север"
} 
sklonenie = {
    0: 0,
    1: 362,
    2: 703,
    3: 1002,
    4: 1238,
    5: 1388,
    6: 1440
}
kranty_mult = {
    0: 362,
    1: 341,
    2: 299,
    3: 236,
    4: 150,
    5: 52,

}


# Ira
"""
ravnodenstvie_distance([266, 43])
ravnodenstvie_distance([250, 56])
ravnodenstvie_distance([283, 34])
ravnodenstvie_distance([266, 56])
ravnodenstvie_distance([298, 55])
ravnodenstvie_distance([285, 32])
ravnodenstvie_distance([348, 44])
"""
# ya
"""
ravnodenstvie_distance([33, 19])
ravnodenstvie_distance([154, 52])
ravnodenstvie_distance([378, 46])
ravnodenstvie_distance([72, 50])
ravnodenstvie_distance([101, 24])
ravnodenstvie_distance([124, 27])
ravnodenstvie_distance([306, 23])
"""