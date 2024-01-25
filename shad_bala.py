from conf import *
from datetime import datetime, timedelta

graha = "Сатурн"
rashi = "Водолей"
minutes = 24
seconds = 56

lagna_minutes = 2
lagna_seconds = 55
lagna_rashi = "Дева"

"""
graha = "Сатурн"
rashi = "Скорпион"
minutes = 22
seconds = 59

graha = "Солнце"
rashi = "Дева"
minutes = 23
seconds = 22

lagna_minutes = 13
lagna_seconds = 57
lagna_rashi = "Лев"

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
в случае превышения 180 или 360 градусов нужно вычитать """
def calculate_dig_bala(
    dolgota_minutes, 
    dolgota_seconds, 
    lagna_minutes=lagna_minutes, 
    lagna_seconds=lagna_seconds,
    lagna_rashi=lagna_rashi,
    graha=graha,
    rashis=rashi_values
    ):
    lagna_dolgota_minutes = rashis[lagna_rashi] * 30 + lagna_minutes
    graha_sum_seconds = dolgota_minutes * 60 + dolgota_seconds 
    lagna_sum_seconds = lagna_dolgota_minutes * 60 + lagna_seconds
    if graha in ["Солнце", "Марс"]:
        house_4_dolgota_seconds = lagna_sum_seconds + 30*3*60
        if house_4_dolgota_seconds > 360*60: house_4_dolgota_seconds = abs(360*60 - house_4_dolgota_seconds)
        res = abs(graha_sum_seconds - house_4_dolgota_seconds)
        print(f"Точка отсутствия силы: {house_4_dolgota_seconds//60}-{house_4_dolgota_seconds%60}")
    elif graha in ["Юпитер", "Меркурий"]:
        house_7_dolgota_seconds = lagna_sum_seconds + 30*6*60
        if house_7_dolgota_seconds > 360*60: house_7_dolgota_seconds = abs(360*60 - house_7_dolgota_seconds)        
        res = abs(graha_sum_seconds - house_7_dolgota_seconds)
        print(f"Точка отсутствия силы: {house_7_dolgota_seconds//60}-{house_7_dolgota_seconds%60}")
    elif graha == "Сатурн":
        res = abs(graha_sum_seconds - lagna_sum_seconds)
        print(f"Точка отсутствия силы: {lagna_sum_seconds//60}-{lagna_sum_seconds%60}")
    elif graha in ["Венера", "Луна"]:
        house_10_dolgota_seconds = lagna_sum_seconds + 30*9*60
        #if house_10_dolgota_seconds > 360*60: house_10_dolgota_seconds = abs(360*60 - house_10_dolgota_seconds)
        #if house_10_dolgota_seconds > 360*60: house_10_dolgota_seconds = abs(house_10_dolgota_seconds-360*60)

        res = abs(graha_sum_seconds - house_10_dolgota_seconds)
        print(f"Точка отсутствия силы: {house_10_dolgota_seconds//60}-{house_10_dolgota_seconds%60}")
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
    dolgota_seconds=dolgota_seconds)

voshod = [6, 32] 
zahod = [18, 19]
day = [11, 47]
night = [12, 12]
day_s = (day[0]*60 + day[1])
birth_time = [3, 48]
birth_time_s = int(birth_time[0]*60 + birth_time[1])
print(day_s/2)
print(f"Продолжительность половины дня: {(day_s/2) // 60}: {(day_s/2) % 60}")

# полдень
half_day = int(voshod[0]*60 + voshod[1] + day_s/2)
half_day_m = half_day//60
half_day_s = half_day%60

print(f"Середина солнечного дня: {half_day_m}:{half_day_s}")
# полночь
polnoch = half_day + 12*60
if polnoch > 24*60: polnoch -= 24*60
half_day_m = polnoch//60
half_day_s = polnoch%60
print(f"Полночь наступает в {half_day_m}:{half_day_s}")

razn = polnoch * birth_time_s
r_m = razn//60
r_s = razn%60
print(f"{r_m}:{r_s}")

# saptavarga
#print(graha_perm_rel)
#print(f"Друзья для {graha}: {graha_perm_rel[graha]['Друг']}")


def time_difference(start_hours, start_minutes, subtract_hours, subtract_minutes, action="subtract"):
    # Переводим часы и минуты в минуты
    start_total_minutes = start_hours * 60 + start_minutes
    subtract_total_minutes = subtract_hours * 60 + subtract_minutes
    if action =="subtract":
    # Вычисляем разницу в минутах
        difference_minutes = start_total_minutes - subtract_total_minutes
    else: 
        difference_minutes = start_total_minutes + subtract_total_minutes
    # Вычисляем часы и минуты из разницы в минутах
    difference_hours = difference_minutes // 60
    difference_minutes %= 60

    return f"{difference_hours}:{difference_minutes:02d}"

# прибавить, вычесть секунды
start_hours = 208
start_minutes = 41
subtract_hours = 59
subtract_minutes = 4

difference = time_difference(start_hours, start_minutes, subtract_hours, subtract_minutes, "+")

print("Разница времени:", difference)

def kala_bala(sunrise, light_day, birth_time):
    # 1 ghati = 24 minutes, 1 palam = 24 seconds
    ghati, palam = 24, 24
    half_day = (light_day[0] * 60 + light_day[1]) / 2
    mid_day = sunrise[0] * 60 + sunrise[1] + half_day
    mid_night = half_day + 12*60

    sunrise_mid_night = int((sunrise[0] * 60 + sunrise[1]) - mid_night)
    sunrise_mid_night = [sunrise_mid_night//60, sunrise_mid_night%60]
    sunrise_birth_time = int((sunrise[0] * 60 + sunrise[1]) - (birth_time[0] * 60 + birth_time[1]))
    sunrise_birth_time = [sunrise_birth_time//60, sunrise_birth_time%60]
    ynatta = time_difference (sunrise_mid_night[0], sunrise_mid_night[1], 
                            sunrise_birth_time[0], sunrise_birth_time[1])
    print(ynatta)                        

kala_bala([7, 55], [8, 3], [23, 45])