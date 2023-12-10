import json

dict_new = {}
with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    for line in f:
        dict_old = json.loads(line)
        key = dict_old['user_id']
        value = dict_old['category']
        dict_new[key] = value

for key, value in dict_new.items():
  print("{0}: {1}".format(key,value))
