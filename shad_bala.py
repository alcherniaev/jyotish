from conf import grahas, rashi_values
graha = "Юпитер"
rashi="Стрелец"
minutes=3
seconds=8

def calculate_dolgota(minutes, seconds, rashi, graha, rashis=rashi_values):
    if rashi in rashis:
        dolgota_minutes = rashis[rashi] * 30 + minutes
        dolgota_seconds = seconds
        print(f"Долгота для {graha} в {rashi} {minutes}-{seconds}: {dolgota_minutes}, {dolgota_seconds}")
        return dolgota_minutes, dolgota_seconds
    else:
        print(f"Ошибка: Не найдено значение для знака '{rashi}' и планеты {graha}")
        return None
    
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


