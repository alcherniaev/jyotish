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
def ravnodenstvie_distance(dolgota, ayanamsha=[21,16] ):
    ayanamsha_minutes = ayanamsha[0]*60 + ayanamsha[1]
    dolgota_minutes = dolgota[0]*60 + dolgota[1]
    dolgota_ayanamsha_minutes = dolgota_minutes + ayanamsha_minutes
    distance = 360*60 - dolgota_ayanamsha_minutes 

    if dolgota_minutes < 90*60: 
        distance = dolgota_minutes
    if dolgota_minutes > 360*60: 
        distance = dolgota_minutes - 360*60
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
    kranty = int(c + 362)
    print(f"kranty = {kranty//60, kranty%60}")
    return kranty/60
kranty = ravnodenstvie_distance([180, 54])
"""ravnodenstvie_distance([332, 33])
ravnodenstvie_distance([250, 47])
ravnodenstvie_distance([202, 48])
ravnodenstvie_distance([105, 17])
ravnodenstvie_distance([192, 26])
ravnodenstvie_distance([145, 39])
"""


def ayana_bala(kranti):
    res = ((24 - kranti) * 60) / 48
    #res = res * 2 # сурья онли x2
    print(f"ayana bala: {res}")

ayana_bala(kranty)
