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
    "Рыба": 11
}


def calculate_dolgota(minutes, seconds, rashi, graha, rashis=rashi_values):
    if rashi in rashis:
        dolgota_minutes = rashis[rashi] * 30 + minutes
        dolgota_seconds = seconds
        print(f"Долгота для {graha} в {rashi} {minutes}-{seconds}: {dolgota_minutes}, {dolgota_seconds}")
        return dolgota_minutes, dolgota_seconds
    else:
        print(f"Ошибка: Не найдено значение для знака '{rashi}' и планеты {graha}")
        return None
    
def calculate_raznitsa(minutes, graha, seconds=0, grahas=grahas):
    gradus_debilitation = grahas[graha]
    raznitsa_minutes = abs(minutes - gradus_debilitation)
    total_seconds_graha = raznitsa_minutes * 60 + seconds
    #print(f"{minutes} минут и {seconds} секунд в сумме равны {result_seconds} секунд.")
    return total_seconds_graha

def convert_to_minutes_and_seconds(total_seconds):
    print("*****")
    total_seconds //= 3
    minutes = total_seconds // 60
    remaining_seconds = total_seconds % 60
    print(f"Учча-Бала: {minutes}.{remaining_seconds}")
    return minutes, remaining_seconds

"""graha = "Солнце"
rashi="Дева"
minutes=23
seconds=23"""
graha = "Луна"
rashi="Телец"
minutes=10
seconds=11

dolgota_minutes, dolgota_seconds = calculate_dolgota(
                                                minutes=minutes, 
                                                seconds=seconds, 
                                                rashi=rashi,
                                                graha=graha)

raznitsa = calculate_raznitsa(
    minutes=dolgota_minutes, 
    graha=graha,
    seconds=dolgota_seconds)

convert_to_minutes_and_seconds(raznitsa)


