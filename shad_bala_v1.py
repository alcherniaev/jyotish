from conf import *
from datetime import datetime, timedelta

# Список планет и их позиций
ayanamsha=[23,39]
planets_info = [
    ("Солнце", "Водолей", [0, 52]),
    ("Луна", "Скорпион", [13, 7]),
    ("Меркурий", "Козерог", [26, 12]),
    ("Венера", "Рыбы", [15, 43]),
    ("Марс", "Рыбы", [14, 17]),
    ("Юпитер", "Козерог", [7, 51]),
    ("Сатурн", "Скорпион", [4, 3])
]
"""print(planets_info[0])
print(planets_info[0][0])
print(planets_info[0][1])
print(planets_info[0][2][0])
print(planets_info[0][2][1])
calculate_dolgota(11, 8, "Лев", "Луна")
"""
planets_info_aleksei = [
    ("Солнце", "Овен", [9, 35]),
    ("Луна", "Лев", [11, 8]),
    ("Меркурий", "Рыбы", [25, 2]),
    ("Венера", "Телец", [19, 6]),
    ("Марс", "Близнецы", [17, 40]),
    ("Юпитер", "Рак", [10, 43]),
    ("Сатурн", "Козерог", [12, 39])
]
planets_info = planets_info_aleksei


lagna_minutes = 28
lagna_seconds = 35
lagna_rashi = "Овен"

sunrise = [8, 9]
light_day = [9, 8]
birth_time = [10, 0]
sunset = [17, 17]

"""lagna_minutes = 10
lagna_seconds = 9
lagna_rashi = "Козерог"
"""

def calculate_dolgota(minutes, seconds, rashi, graha, rashis=rashi_values, initial=True):
    if rashi in rashis:
        dolgota_minutes = rashis[rashi] * 30 + minutes
        dolgota_seconds = seconds
        if initial: 
            print(f"Долгота для {graha} в {rashi} {minutes}-{seconds}: {dolgota_minutes}, {dolgota_seconds}")

        return dolgota_minutes, dolgota_seconds
    else:
        print(f"Ошибка: Не найдено значение для знака '{rashi}' и планеты {graha}")
        return None

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
    elif graha in ["Юпитер", "Меркурий"]:
        house_7_dolgota_seconds = lagna_sum_seconds + 30*6*60
        if house_7_dolgota_seconds > 360*60: 
            house_7_dolgota_seconds = abs(360*60 - house_7_dolgota_seconds)        
        res = abs(graha_sum_seconds - house_7_dolgota_seconds)
    elif graha == "Сатурн":
        res = abs(graha_sum_seconds - lagna_sum_seconds)
    elif graha in ["Венера", "Луна"]:
        house_10_dolgota_seconds = lagna_sum_seconds + 30*9*60
        if house_10_dolgota_seconds > 360*60: house_10_dolgota_seconds = abs(360*60 - house_10_dolgota_seconds)

        res = abs(graha_sum_seconds - house_10_dolgota_seconds)
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
    return result_seconds


def convert_to_minutes_and_seconds(total_seconds):
    print("*****")
    total_seconds //= 3
    minutes = total_seconds // 60
    remaining_seconds = total_seconds % 60
    print(f"Учча-Бала: {minutes}.{remaining_seconds}")
    return
    #return minutes, remaining_seconds


def kala_bala(sunrise, light_day, birth_time):
    # разница между временем рождения и полночью
    # 1 ghati = 24 minutes, 1 palam = 24 seconds
    ghati, palam = 24, 24
    half_light_day = (light_day[0] * 60 + light_day[1]) / 2
    mid_day = sunrise[0] * 60 + sunrise[1] + half_light_day
    mid_night = mid_day + 12*60
    print(f"mid_night: {[mid_night//60, mid_night%60]}")

    birth_time_minutes = birth_time[0] * 60 + birth_time[1]
    unnata_bala = abs(birth_time_minutes - mid_night)
    nata_bala = abs(720 - unnata_bala)
    chandra_mangala_shani = nata_bala * 2
    syria_guru = 1440 - chandra_mangala_shani
    chandra_mangala_shani_ghati = [int(chandra_mangala_shani // 24), int((chandra_mangala_shani%24)*60/24)]
    syria_guru_shukra_ghati = [int(syria_guru // 24), int((syria_guru%24)*60/24)]
    print("")
    print("******* Nathonata Bala *******")
    print(f"chandra, mangala, shani: {chandra_mangala_shani_ghati}")
    print(f"syria, guru, shukra: {syria_guru_shukra_ghati}")
    print("Buddhi: 60")
    print("")
    return


def subtract_astronomical_time(min1, sec1, min2, sec2, diff_360=0):
    total_min1 = min1 + sec1 / 60
    total_min2 = min2 + sec2 / 60
    diff_min = total_min1 - total_min2
    if diff_min < 0 and diff_360 == 0:
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

def paksha_bala(syria, chandra):
    chandra_dolgota = [0,0]
    syria_dolgota = [0,0]
    chandra_dolgota[0], chandra_dolgota[1] = calculate_dolgota(chandra[2][0], chandra[2][1], chandra[1], chandra[0], initial=False)
    syria_dolgota[0], syria_dolgota[1] = calculate_dolgota(syria[2][0], syria[2][1], syria[1], syria[0], initial=False)
    
    good_planet_bala = subtract_astronomical_time(chandra_dolgota[0], chandra_dolgota[1], syria_dolgota[0], syria_dolgota[1])
    if good_planet_bala[0] > 180:
        good_planet_bala = subtract_astronomical_time(360, 0, good_planet_bala[0], good_planet_bala[1])
    good_planet_bala = divide_astronomical_degrees(good_planet_bala[0], good_planet_bala[1], 3)
    bad_planet_bala = subtract_astronomical_time(60, 0, good_planet_bala[0], good_planet_bala[1])
    print("******* Paksha Bala *******")
    print(f"Сила Благотворных планет: {good_planet_bala}")
    print(f"Сила Зловредных планет: {bad_planet_bala}")
    print("")

def birth_period(sunrise, sunset, birth_time, light_day):
    print("******* Tribhata Bala *******")
    # пока выводим день/ночь и их интервалы. 
    #TODO следует помониторить и после автоматизировать
    sunrise_minutes = sunrise[0] * 60 + sunrise[1]
    sunset_minutes = sunset[0] * 60 + sunset[1]
    birth_time_minutes = birth_time[0] * 60 + birth_time[1]
    light_day_minutes = light_day[0] * 60 + light_day[1]

    # Проверяем, если время рождения находится между восходом и закатом
    if sunrise_minutes <= birth_time_minutes <= sunset_minutes:
        print("день,", end=" ")
        # Разделяем световой день на 3 равные части
        day_third = light_day_minutes / 3
        """if birth_time_minutes <= day_third:
            print("1 треть")
        elif day_third < birth_time_minutes <= 2 * day_third:
            print("2 треть")
        else:
            print("3 треть")"""

        print(f"длительность дня: {light_day_minutes} минут")
        print(f"треть дня: {day_third}")

        third_1 = [int((sunrise_minutes + day_third)//60), int((sunrise_minutes + day_third)%60)]
        if third_1[0]*60 + third_1[1] > 24*60:
            third_1_p = 24*60 - (third_1[0]*60 + third_1[1])
            third_1 = [third_1_p[0], third_1_p[1]]

        third_2 = [int((sunrise_minutes + day_third*2)//60), int((sunrise_minutes + day_third*2)%60)]
        if third_2[0]*60 + third_2[1] > 24*60:
            third_2_p = (third_2[0]*60 + third_2[1]) - 24*60
            third_2 = [third_2_p//60, third_2_p%60]

        third_3 = [int((sunrise_minutes + day_third*3)//60), int((sunrise_minutes + day_third*3)%60)]
        if third_3[0]*60 + third_3[1] > 24*60:
            third_3_p = (third_3[0]*60 + third_3[1]) - 24*60
            third_3 = [third_3_p//60, third_3_p%60]

        print(f"Первая треть дня: {sunrise[0]}:{sunrise[1]} - {third_1[0]}:{third_1[1]} (Меркурий)")
        print(f"Вторая треть дня: {third_1[0]}:{third_1[1]} - {third_2[0]}:{third_2[1]} (Сурья)")
        print(f"Третья треть дня: {third_2[0]}:{third_2[1]} - {third_3[0]}:{third_3[1]} (Шани)")

    else:
        print("ночь,", end=" ")
        # Рассчитываем продолжительность ночи
        night_duration = 24 * 60 - light_day_minutes
        # Определяем время начала ночи
        night_start = sunset_minutes #if sunset_minutes < sunrise_minutes else sunrise_minutes
        # Разделяем ночь на 3 равные части относительно времени начала ночи
        night_third = night_duration / 3
        print(f"длительность ночи: {night_duration} минут")
        print(f"треть ночи: {night_third}")
        third_1 = [int((night_start + night_third)//60), int((night_start + night_third)%60)]
        if third_1[0]*60 + third_1[1] > 24*60:
            third_1_p = 24*60 - (third_1[0]*60 + third_1[1])
            third_1 = [third_1_p[0], third_1_p[1]]

        third_2 = [int((night_start + night_third*2)//60), int((night_start + night_third*2)%60)]
        if third_2[0]*60 + third_2[1] > 24*60:
            third_2_p = (third_2[0]*60 + third_2[1]) - 24*60
            third_2 = [third_2_p//60, third_2_p%60]

        third_3 = [int((night_start + night_third*3)//60), int((night_start + night_third*3)%60)]
        if third_3[0]*60 + third_3[1] > 24*60:
            third_3_p = (third_3[0]*60 + third_3[1]) - 24*60
            third_3 = [third_3_p//60, third_3_p%60]

        print(f"Первая треть ночи: {sunset[0]}:{sunset[1]} - {third_1[0]}:{third_1[1]} (Луна)")
        print(f"Вторая треть ночи: {third_1[0]}:{third_1[1]} - {third_2[0]}:{third_2[1]} (Венера)")
        print(f"Третья треть ночи: {third_2[0]}:{third_2[1]} - {third_3[0]}:{third_3[1]} (Марс)")
    print(f"Юпитер всегда + 60")

def ayana_bala(kranti, graha, rashi):
    """
    Для Солнца, Марса, Юпитера и Венеры — при северном склонении осуществляется сложение кранти, при южном – вычитание.
    Для Луны и Сатурна — при северном склонении осуществляется вычитание кранти, при южном – сложение.
    Для Меркурия кранти всегда прибавляется. Для Солнца аяна бала удваивается.
    """
    print(f"Направление: {graha_direction[rashi]}")
    if graha in ("Солнце", "Марс", "Юпитер", "Венера") and graha_direction[rashi] == "Север": 
        res = ((24 + kranti) * 60) / 48
        
    if graha in ("Солнце", "Марс", "Юпитер", "Венера") and graha_direction[rashi] == "ЮГ": 
        res = ((24 - kranti) * 60) / 48

    if graha in ("Луна", "Сатурн") and graha_direction[rashi] == "Север": 
        res = ((24 - kranti) * 60) / 48
    if graha in ("Луна", "Сатурн") and graha_direction[rashi] == "ЮГ": 
        res = ((24 + kranti) * 60) / 48
    if graha == "Меркурий": 
        res = ((24 + kranti) * 60) / 48 
    if graha == "Солнце": 
        res = res * 2 # сурья онли x2
    print(f"ayana bala: {int(res)}")


def ravnodenstvie_distance(dolgota, ayanamsha=[21,16]):
    ayanamsha_minutes = ayanamsha[0]*60 + ayanamsha[1]
    dolgota_minutes = dolgota[0]*60 + dolgota[1]
    dolgota_ayanamsha_minutes = dolgota_minutes + ayanamsha_minutes
    distance = 360*60 - dolgota_ayanamsha_minutes 

    if dolgota_ayanamsha_minutes < 90*60: 
        distance = dolgota_ayanamsha_minutes
    if dolgota_ayanamsha_minutes > 360*60: 
        distance = dolgota_ayanamsha_minutes - 360*60

    if distance > 180*60: 
        distance = 180*60 - dolgota_ayanamsha_minutes 
    if distance > 90*60 and distance < 180*60:
        distance = 180*60 - distance
    if distance < 90*60 and distance > 0: 
        print(distance//60, distance%60)
    else:
        raise ValueError(f"ошибка при расчете: bhudja = {distance//60, distance%60}")


    bhudja = [distance//60, distance%60]
    bhudja_ostatok = bhudja[0]//15
    bhudja_chastnoe = [bhudja[0]%15, bhudja[1]]
    print(f"bhudja_ostatok = {bhudja_ostatok}")
    print(f"bhudja_chastnoe = {bhudja_chastnoe}")
    a = (bhudja_chastnoe[0]*60+bhudja_chastnoe[1])
    b = 15*60
    c = (a/b) * kranty_mult[bhudja_ostatok]
    kranty = int(c + sklonenie[bhudja_ostatok])
    print(f"kranty = {kranty//60, kranty%60}")
    return kranty/60


"""
год, месяц, день, хора
Важно, чтобы год начинался до даты рождения (новолуние чайтра)
день не календарный, типа понедельник, а от даты восхода. 
может и воскресенье еще действовать в понедельник    
"""





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

    kranti = ravnodenstvie_distance([dolgota_minutes,dolgota_seconds], ayanamsha=ayanamsha)
    ayana_bala(kranti=kranti, graha=graha, rashi=rashi)
    print("*****************************************")

kala_bala(sunrise, light_day, birth_time)

paksha_bala(planets_info[0], planets_info[1])
birth_period(sunrise, sunset, birth_time, light_day)

print("DRAFTS**********")
subtract_astronomical_time(344, 17, 300, 52, diff_360=1)
#subtract_astronomical_time(9, 35, 131, 8, diff_360=1)