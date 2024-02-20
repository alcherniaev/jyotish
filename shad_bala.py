from conf import *
from datetime import datetime, timedelta

#Планеты
################################### 
graha = "Солнце"
rashi = "Водолей"
position = [0, 52]
minutes = position[0]
seconds = position[1]

graha = "Луна"
rashi = "Скорпион"
position = [13, 7]
minutes = position[0]
seconds = position[1]

graha = "Меркурий"
rashi = "Козерог"
position = [26, 12]
minutes = position[0]
seconds = position[1]

graha = "Венера"
rashi = "Рыбы"
position = [15, 43]
minutes = position[0]
seconds = position[1]

graha = "Марс"
rashi = "Рыбы"
position = [14, 17]
minutes = position[0]
seconds = position[1]

graha = "Юпитер"
rashi = "Козерог"
position = [7, 51]
minutes = position[0]
seconds = position[1]

graha = "Сатурн"
rashi = "Скорпион"
position = [4, 3]
minutes = position[0]
seconds = position[1]
###################################


lagna_minutes = 28
lagna_seconds = 35
lagna_rashi = "Овен"


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
    graha=graha,
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

#sunrise, light_day, birth_time
voshod = [4, 51] 
zahod = [20, 3]
day = [15, 12]
night = [8, 48]
day_s = (day[0]*60 + day[1])
birth_time = [3, 48]
birth_time_s = int(birth_time[0]*60 + birth_time[1])
print(day_s/2)
print("----")
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
print("----")
razn = polnoch * birth_time_s
r_m = razn//60
r_s = razn%60
print(f"{r_m}:{r_s}")

# saptavarga
#print(graha_perm_rel)
#print(f"Друзья для {graha}: {graha_perm_rel[graha]['Друг']}")


def time_difference(start_hours, start_minutes, subtract_hours, subtract_minutes, action="subtract", d=False):
    # Переводим часы и минуты в минуты
    start_total_minutes = start_hours * 60 + start_minutes
    subtract_total_minutes = subtract_hours * 60 + subtract_minutes
    if action =="subtract" or action == "-":
    # Вычисляем разницу в минутах
        difference_minutes = start_total_minutes - subtract_total_minutes
    else: 
        difference_minutes = start_total_minutes + subtract_total_minutes
    if d == True: 
        if difference_minutes < 0: # после достижения 0 начинается не 0, а 360, не -1, а 359 и тд
           difference_minutes = 360*60 + difference_minutes
    # Вычисляем часы и минуты из разницы в минутах
    difference_hours = difference_minutes // 60
    difference_minutes %= 60
    
        
    return f"{difference_hours}:{difference_minutes:02d}"

# прибавить, вычесть секунды
start_hours = 355
start_minutes = 26
subtract_hours = 9
subtract_minutes = 44

action = "-"


difference = time_difference(start_hours, start_minutes, subtract_hours, subtract_minutes, action, d=False)

print("Разница времени:", difference)

# TODO
sunrise = [4, 51]
light_day = [15, 12]
birth_time = [3, 10]
def kala_bala(sunrise, light_day, birth_time):
    # разница между временем рождения и полночью
    # 1 ghati = 24 minutes, 1 palam = 24 seconds
    ghati, palam = 24, 24
    half_light_day = (light_day[0] * 60 + light_day[1]) / 2
    print(f'half_light_day: {half_light_day}')
    print(f'half_light_day: {[half_light_day//60, half_light_day%60]}')
    #half_light_day = [half_day//60, half_day%60]
    mid_day = sunrise[0] * 60 + sunrise[1] + half_light_day
    print(f"mid_day: {[mid_day//60, mid_day%60]}")
    mid_night = half_day + 12*60
    print(f"mid_night: {[mid_night//60, mid_night%60]}")

    # отсюда разница между восходом и полночью, и временем рождения !
    birth_time_minutes = birth_time[0] * 60 + birth_time[1]
    mid_night_minutes = mid_night#[0] * 60 + mid_night[1]
    unnata_bala = abs(birth_time_minutes - mid_night_minutes)
    
    nata_bala = abs(720 - unnata_bala)
    chandra_mangala_shani = nata_bala * 2

    syria_guru = 1440 - chandra_mangala_shani
    chandra_mangala_shani_ghati = [chandra_mangala_shani // 24, (chandra_mangala_shani%24)*60/24]
    syria_guru_ghati = [syria_guru // 24, (syria_guru%24)*60/24]
    print(f"chandra, mangala, shani: {chandra_mangala_shani_ghati}")
    print(f"syria, guru: {syria_guru_ghati}")
    print("Buddhi: 60")

    sunrise_mid_night = max(
        int(mid_night - (sunrise[0] * 60 + sunrise[1])),
        int((sunrise[0] * 60 + sunrise[1]) - mid_night))
    print(f"sunrise_mid_night: {sunrise_mid_night}")
    #sunrise_mid_night = [sunrise_mid_night//60, sunrise_mid_night%60]
    sunrise_birth_time = max(
        int((birth_time[0] * 60 + birth_time[1]) - (sunrise[0] * 60 + sunrise[1])),
        int((sunrise[0] * 60 + sunrise[1]) - (birth_time[0] * 60 + birth_time[1])))
    #sunrise_birth_time = [sunrise_birth_time//60, sunrise_birth_time%60]
    print(f"sunrise_birth_time: {sunrise_birth_time}")
    #ynatta = time_difference (sunrise_mid_night[0], sunrise_mid_night[1], 
    #                        sunrise_birth_time[0], sunrise_birth_time[1])
    """sunrise_mid_night = int(mid_night - (sunrise[0] * 60 + sunrise[1]) )
    sunrise_mid_night = [sunrise_mid_night//60, sunrise_mid_night%60]
    sunrise_birth_time = int((birth_time[0] * 60 + birth_time[1]) - (sunrise[0] * 60 + sunrise[1]))
    sunrise_birth_time = [sunrise_birth_time//60, sunrise_birth_time%60]
    ynatta = time_difference (sunrise_mid_night[0], sunrise_mid_night[1], 
                            sunrise_birth_time[0], sunrise_birth_time[1])"""
    print(sunrise_mid_night)
    print(sunrise_birth_time)
    #print(f"ynatta: {ynatta}")                        

#kala_bala([7, 55], [8, 3], [23, 45])
kala_bala(sunrise, light_day, birth_time)

def subtract_astronomical_time(min1, sec1, min2, sec2):
    total_min1 = min1 + sec1 / 60
    total_min2 = min2 + sec2 / 60
    diff_min = total_min1 - total_min2
    if diff_min < 0:
        diff_min += 360  # Учитываем зацикленность по 360 градусам
    diff_sec = (diff_min - int(diff_min)) * 60
    diff_min = int(diff_min)
    return [diff_min, int(diff_sec)]

def divide_astronomical_degrees(minutes, seconds, divisor=15):
    divisor = divisor
    total_minutes = minutes * 60 + seconds 
    divided_minutes = total_minutes / divisor
    result_minutes = divided_minutes // 60
    result_seconds = divided_minutes % 60
    
    return [int(result_minutes), int(result_seconds)]

def paksha_bala():
    chandra = [0,0]
    syria = [0,0]
    chandra[0], chandra[1] = calculate_dolgota(11, 8, "Лев", "Луна")
    syria[0], syria[1] = calculate_dolgota(9, 35, "Овен", "Солнце")
    
    good_planet_bala = subtract_astronomical_time(chandra[0], chandra[1], syria[0], syria[1])
    if good_planet_bala[0] > 180:
        good_planet_bala = subtract_astronomical_time(360, 0, good_planet_bala[0], good_planet_bala[1])
    good_planet_bala = divide_astronomical_degrees(good_planet_bala[0], good_planet_bala[1], 3)
    bad_planet_bala = subtract_astronomical_time(60, 0, good_planet_bala[0], good_planet_bala[1])
    print(f"Сила Благотворных планет: {good_planet_bala}")
    print(f"Сила Зловредных планет: {bad_planet_bala}")

paksha_bala()




bhudja = [55, 50]
print(f"devided: {bhudja[0]//15}")
#print(f"devided: {1302//60}")

#print(f"devided: {1302//60}")
#print(f"devided: {1302%60}")
print("asd", divide_astronomical_degrees(5, 30, 4))
a = (8*60 + 37)
b = 15*60 
c = (a/b) * 236
d = int(c + 1002)
print(f"a={a}, b={b}, c={c}. d={d}")
print(d // 60, d%60)

def ayana_bala(kranti):
    res = ((24 - kranti) * 60) / 48
    #res = res * 2 # сурья онли x2
    print(f"ayana bala: {res}")
    
    
ayana_bala(18.57)
#print(0.6499999999999995 * 2) 
print(74.28//15)
print(74.28%15)

print("\033[1mЖирный текст\033[0m")
def time_difference_2(birth_time, sunrise_time):
    birth_hours, birth_minutes = birth_time[0], birth_time[1]
    sunrise_hours, sunrise_minutes = sunrise_time[0], sunrise_time[1]

    # Преобразуем время в минуты
    birth_total_minutes = birth_hours * 60 + birth_minutes
    sunrise_total_minutes = sunrise_hours * 60 + sunrise_minutes

    # Вычисляем разницу
    difference_minutes = sunrise_total_minutes - birth_total_minutes

    # Обработка случая, когда время восхода солнца позже времени рождения
    if difference_minutes < 0:
        difference_minutes += 24 * 60  # Добавляем 24 часа в минутах

    return difference_minutes

# Пример использования функции
birth_time = [3,10]
sunrise_time = [4, 51]

difference = time_difference_2(birth_time, sunrise_time)
print("Разница между временем восхода солнца и временем рождения:", difference, "минут")
print(1277//24)
print((1263%24))
print(1488//60)
print((1488%60))