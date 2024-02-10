from conf import *
from datetime import datetime, timedelta

# Список планет и их позиций
planets_info = [
    ("Солнце", "Водолей", [0, 52]),
    ("Луна", "Скорпион", [13, 7]),
    ("Меркурий", "Козерог", [26, 12]),
    ("Венера", "Рыбы", [15, 43]),
    ("Марс", "Рыбы", [14, 17]),
    ("Юпитер", "Козерог", [7, 51]),
    ("Сатурн", "Скорпион", [4, 3])
]

planets_info_aleksei = [
    ("Солнце", "Овен", [9, 35]),
    ("Луна", "Лев", [11, 8]),
    ("Меркурий", "Рыбы", [25, 2]),
    ("Венера", "Телец", [19, 6]),
    ("Марс", "Близнецы", [17, 40]),
    ("Юпитер", "Рак", [10, 43]),
    ("Сатурн", "Козерог", [12, 39])
]


lagna_minutes = 28
lagna_seconds = 35
lagna_rashi = "Овен"

"""lagna_minutes = 10
lagna_seconds = 9
lagna_rashi = "Козерог"
"""

def calculate_dolgota(minutes, seconds, rashi, graha, rashis=rashi_values):
    if rashi in rashis:
        dolgota_minutes = rashis[rashi] * 30 + minutes
        dolgota_seconds = seconds
        print(f"Долгота для {graha} в {rashi} {minutes}-{seconds}: {dolgota_minutes}, {dolgota_seconds}")

        return dolgota_minutes, dolgota_seconds
    else:
        print(f"Ошибка: Не найдено значение для знака '{rashi}' и планеты {graha}")
        return None
    
"""нуждается в сверке / корректировке расчета (стр. 449)
в случае превышения 180 или 360 градусов нужно вычитать (360 проверил)"""
def calculate_dig_bala(
    dolgota_minutes, 
    dolgota_seconds, 
    lagna_minutes=lagna_minutes, 
    lagna_seconds=lagna_seconds,
    lagna_rashi=lagna_rashi,
    graha=None,  # Мы добавляем graha в список аргументов и устанавливаем значение по умолчанию None
    rashis=rashi_values
    ):
    lagna_dolgota_minutes = rashis[lagna_rashi] * 30 + lagna_minutes
    graha_sum_seconds = dolgota_minutes * 60 + dolgota_seconds 
    lagna_sum_seconds = lagna_dolgota_minutes * 60 + lagna_seconds
    if graha in ["Солнце", "Марс"]:
        house_4_dolgota_seconds = lagna_sum_seconds + 30*3*60
        if house_4_dolgota_seconds > 360*60: 
            house_4_dolgota_seconds = abs(360*60 - house_4_dolgota_seconds)
        res = abs(graha_sum_seconds - house_4_dolgota_seconds)
        print(f"Точка отсутствия силы: {house_4_dolgota_seconds//60}-{house_4_dolgota_seconds%60}")
    elif graha in ["Юпитер", "Меркурий"]:
        house_7_dolgota_seconds = lagna_sum_seconds + 30*6*60
        if house_7_dolgota_seconds > 360*60: 
            house_7_dolgota_seconds = abs(360*60 - house_7_dolgota_seconds)        
        res = abs(graha_sum_seconds - house_7_dolgota_seconds)
        print(f"Точка отсутствия силы: {house_7_dolgota_seconds//60}-{house_7_dolgota_seconds%60}")
    elif graha == "Сатурн":
        res = abs(graha_sum_seconds - lagna_sum_seconds)
        print(f"Точка отсутствия силы: {lagna_sum_seconds//60}-{lagna_sum_seconds%60}")
    elif graha in ["Венера", "Луна"]:
        house_10_dolgota_seconds = lagna_sum_seconds + 30*9*60
        if house_10_dolgota_seconds > 360*60: house_10_dolgota_seconds = abs(360*60 - house_10_dolgota_seconds)
        #if house_10_dolgota_seconds > 360*60: house_10_dolgota_seconds = abs(house_10_dolgota_seconds-360*60)

        res = abs(graha_sum_seconds - house_10_dolgota_seconds)
        print(f"Точка отсутствия силы: {house_10_dolgota_seconds//60}-{house_10_dolgota_seconds%60}")
    print(f"Результат, который если больше 180, нужно его вычесть из 180 или 360(!): {res//60}") 
    if res  > 180*60:
        res = abs(360*60 - res)
        print(f"Новый Результат, (вычтен из 360) (!): {res//60}")
    res //= 3
    minutes = res // 60
    remaining_seconds = res % 60
    print("*****")
    print(f"Диг-Бала: {minutes}.{remaining_seconds}")
    return minutes, remaining_seconds
    


def calculate_raznitsa(dolgota_minutes, graha, dolgota_seconds=0, grahas=grahas):

    gradus_debilitation = grahas[graha]
    initial_seconds_total = dolgota_minutes * 60 + dolgota_seconds
    result_seconds = abs(initial_seconds_total - gradus_debilitation * 60)
    if result_seconds // 60 > 180:
        result_seconds = abs(result_seconds - 360*60)
    print(f"Разница по модулю: {result_seconds // 60} минут {result_seconds % 60} секунд")
    return result_seconds


def convert_to_minutes_and_seconds(total_seconds):
    print("*****")
    total_seconds //= 3
    minutes = total_seconds // 60
    remaining_seconds = total_seconds % 60
    print(f"Учча-Бала: {minutes}.{remaining_seconds}")
    return
    #return minutes, remaining_seconds


for planet_info in planets_info:
    graha, rashi, position = planet_info
    minutes, seconds = position

    dolgota_minutes, dolgota_seconds = calculate_dolgota(
                                                minutes=minutes, 
                                                seconds=seconds, 
                                                rashi=rashi,
                                                graha=graha)

    raznitsa = calculate_raznitsa(
        dolgota_minutes=dolgota_minutes, 
        graha=graha,
        dolgota_seconds=dolgota_seconds)

    convert_to_minutes_and_seconds(raznitsa)

    calculate_dig_bala(
        dolgota_minutes=dolgota_minutes, 
        dolgota_seconds=dolgota_seconds,
        graha=graha)  
    print("*****************************************")
