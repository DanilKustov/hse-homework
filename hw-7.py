import re

car_id = 'А222ВС965'
result = re.findall(r'^[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}\d{2,3}$', car_id)
res = result[0]
print(f"Номер {res[0:6]} валиден. Регион: {res[6:]}" if result else "Номер не валиден")
