from conf import *
from datetime import datetime, timedelta

# Список планет и их позиций
ayanamsha=[24,0]
planets_info = [
    ("Солнце", "Овен", [13, 13]),
    ("Луна", "Весы", [1, 19]),
    ("Меркурий", "Овен", [14, 58]),
    ("Венера", "Телец", [8, 56]),
    ("Марс", "Рак", [17, 9]),
    ("Юпитер", "Водолей", [29, 5]),
    ("Сатурн", "Дева", [4, 43]),
#    ("Раху", "Стрелец", [20, 18]),
#    ("Кету", "Близнецы", [20, 18])
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

planets_info_irina = [
    ("Солнце", "Стрелец", [4, 41]),
    ("Луна", "Скорпион", [17, 8]),
    ("Меркурий", "Стрелец", [19, 46]),
    ("Венера", "Козерог", [5, 7]),
    ("Марс", "Стрелец", [21, 44]),
    ("Юпитер", "Стрелец", [3, 8]),
    ("Сатурн", "Водолей", [24, 56])
]
planets_info = planets_info

#denis
lagna_minutes = 19
lagna_seconds = 56
lagna_rashi = "Дева"

#olga
"""sunrise = [8, 9]
light_day = [9, 8]
birth_time = [10, 0]
sunset = [17, 17]"""

sunrise = [4, 42]
light_day = [15, 30]
birth_time = [17, 35]
sunset = [20, 12]

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
    chandra_mangala_shani_ghati = [round(chandra_mangala_shani // 24), round((chandra_mangala_shani%24)*60/24)]
    syria_guru_shukra_ghati = [round(syria_guru // 24), round((syria_guru%24)*60/24)]
    print("")
    print("******* Nathonata Bala *******")
    print(f"chandra, mangala, shani: {chandra_mangala_shani_ghati}")
    print(f"syria, guru, shukra: {syria_guru_shukra_ghati}")
    print("Buddhi: 60")
    print("")
    return


def subtract_astronomical_time(min1, sec1, min2, sec2, diff_360=0):
    total_sec1 = min1*60 + sec1
    total_sec2 = min2*60 + sec2
    diff_sec = total_sec1 - total_sec2
    if diff_sec < 0 and diff_360 == 0:
        diff_sec += 360*60  # Учитываем зацикленность по 360 градусам
    #diff_sec = (diff_min - int(diff_min)) * 60
    #diff_min = int(diff_min)
    return [diff_sec//60, diff_sec%60]


def divide_astronomical_degrees(minutes, seconds, divisor=15):
    divisor = divisor
    total_minutes = minutes * 60 + seconds 
    divided_minutes = total_minutes / divisor
    result_minutes = divided_minutes // 60
    result_seconds = divided_minutes % 60
    
    return [round(result_minutes), round(result_seconds)]

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

        third_1 = [round((sunrise_minutes + day_third)//60), round((sunrise_minutes + day_third)%60)]
        if third_1[0]*60 + third_1[1] > 24*60:
            third_1_p = 24*60 - (third_1[0]*60 + third_1[1])
            third_1 = [third_1_p[0], third_1_p[1]]

        third_2 = [round((sunrise_minutes + day_third*2)//60), round((sunrise_minutes + day_third*2)%60)]
        if third_2[0]*60 + third_2[1] > 24*60:
            third_2_p = (third_2[0]*60 + third_2[1]) - 24*60
            third_2 = [third_2_p//60, third_2_p%60]

        third_3 = [round((sunrise_minutes + day_third*3)//60), round((sunrise_minutes + day_third*3)%60)]
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
        third_1 = [round((night_start + night_third)//60), round((night_start + night_third)%60)]
        if third_1[0]*60 + third_1[1] > 24*60:
            third_1_p = 24*60 - (third_1[0]*60 + third_1[1])
            third_1 = [third_1_p[0], third_1_p[1]]

        third_2 = [round((night_start + night_third*2)//60), round((night_start + night_third*2)%60)]
        if third_2[0]*60 + third_2[1] > 24*60:
            third_2_p = (third_2[0]*60 + third_2[1]) - 24*60
            third_2 = [third_2_p//60, third_2_p%60]

        third_3 = [round((night_start + night_third*3)//60), round((night_start + night_third*3)%60)]
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
    kranty = round(c + sklonenie[bhudja_ostatok])
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
    print("^^^*****Дришти Бала*****^^^")
    """
    Вычитаем аспектирующую из аспектируемой
    Особый аспект Сатурна: 45 (3, 10 дома)
    Особый аспект Юпитер: 30 (5, 9 дома)
    Особый аспект Марс: 15 (4, 8 дома)
    """ 
    for planet_info_2 in planets_info:
        graha_2, rashi_2, position_2 = planet_info_2
        minutes_2, seconds_2 = position_2
        
        dolgota_minutes_2, dolgota_seconds_2 = calculate_dolgota(
                                                    minutes=minutes_2, 
                                                    seconds=seconds_2, 
                                                    rashi=rashi_2,
                                                    graha=graha_2,
                                                    initial=False)
        
        if graha != graha_2:
            pre_drishti = subtract_astronomical_time(dolgota_minutes_2, dolgota_seconds_2, 
                                dolgota_minutes, dolgota_seconds, diff_360=0)
            #drishti_min = drishti[0]*60 + drishti[1]
            pre_drishti_min = pre_drishti[0]*60 + pre_drishti[1]
            drishti = 0
            if 180 < pre_drishti[0] < 300: 
                drishti = (300*60 - pre_drishti_min) / 2
            elif 150 < pre_drishti[0] < 180: 
                drishti = (pre_drishti_min - 150*60) * 2
            elif 120 < pre_drishti[0] < 150: 
                drishti = 150*60 - pre_drishti_min
            elif 90 < pre_drishti[0] < 120: 
                drishti = ((120*60 - pre_drishti_min) / 2) + 30*60
            elif 60 < pre_drishti[0] < 90: 
                drishti = (pre_drishti_min  - 60*60) + 15*60
            elif 30 < pre_drishti[0] < 60: 
                drishti = (pre_drishti_min  - 30*60) / 2
            print(f"Аспект от {graha} На {graha_2} : {round(drishti//60), round(drishti%60)} \n Угол({pre_drishti})")
    print("*****************************************")

kala_bala(sunrise, light_day, birth_time)

paksha_bala(planets_info[0], planets_info[1])
birth_period(sunrise, sunset, birth_time, light_day)







print("DRAFTS**********")


#subtract_astronomical_time(32, 45, 41, 49, diff_360=1)


def time_difference(start_hours, start_minutes, subtract_hours, subtract_minutes, action="subtract", d=False):
    # Переводим часы и минуты в минуты
    start_total_minutes = start_hours * 60 + start_minutes
    subtract_total_minutes = subtract_hours * 60 + subtract_minutes
    print(f"start_total_minutes: {start_total_minutes}")
    print(f"subtract_total_minutes: {subtract_total_minutes}")
    if action =="subtract" or action == "-":
    # Вычисляем разницу в минутах
        difference_minutes = start_total_minutes - subtract_total_minutes
    else: 
        difference_minutes = start_total_minutes + subtract_total_minutes
    if d == True: 
        if difference_minutes < 0: # после достижения 0 начинается не 0, а 360, не -1, а 359 и тд
           difference_minutes = 360*60 + difference_minutes
    # Вычисляем часы и минуты из разницы в минутах
    if difference_minutes > 0:
        print(f"difference_minutes: {difference_minutes}")
        difference_hours = difference_minutes // 60
        difference_minutes %= 60
    else:
        difference_hours = difference_minutes // -60
        difference_hours = 0 - difference_hours
        difference_minutes %= -60
    
        
    return f"{difference_hours}:{difference_minutes:02d}"

# прибавить, вычесть секунды
start_hours = 360
start_minutes = 0
subtract_hours = 304
subtract_minutes = 56
action = "-"

difference = time_difference(start_hours, start_minutes, 
                             subtract_hours, subtract_minutes, action, d=False)
print("Разница времени:", difference)
"""
#Солнце
36.57
10
15
2
10
10
10
30
30
15
59.14
47.45
34.05
30
93
93
60
-2.16

585.45

#Луна
3.22
4
10
15
15
10
15
15
30
25.09
12.15
51.50
57
51.50
51
-0.24

315.04

#Меркурий (сожжен)
16.16
30
45
30
4
15
60
29.12
60
25.55
60
45
48
45
26
-13.31

552.54

#Венера
56.14
14
15
59
15
30
15
15.42
46.25
25.55
34
8.34

334.50

#Марс
44.34
20
4
15
30
2
10
15
44.46
12.15
34.05
33
8.12

272.52

#Юпитер
0.57
15
2
40
17
60
15
23.05
47.45
25.55
60
15
55
-12.43

363.59

#Шани
55.19
12
44
45
45
58.10
12.15
34.05
60
55
0.04

375.45
"""
print(763//60, 763%60)
grds_m = (55*60+4)
grds_m = grds_m*5 / 6
grds = [grds_m//60, grds_m%60]
print(grds)
print(grds[0]//30)
