
# things = '''
# карандаш, 20
# зеркальце, 100
# зонт, 500
# рубашка, 300
# брюки, 1000
# бумага, 200
# молоток, 600
# пила, 400
# удочка, 1200
# расческа, 40
# котелок, 820
# палатка, 5240
# брезент, 2130
# спички, 10
# '''
# things

# things = things.strip().splitlines()


# all_dict = {}
# for thing in things:
#     name, weigth = thing.split(', ')
   
#     all_dict[int(weigth)] = name
    
 
# all_dict = dict(sorted(all_dict.items(), reverse=1))

# bug = []
# s = 0
# for key, value in all_dict.items():
#     if s + key <= 10000:
#         s += key    
#         bug.append(value)   

# print(bug) 


# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}




# new_d = {}

# for key, value in things.items():
#     new_d[value] = key

    
# new_d = dict(sorted(new_d.items(), reverse=1))


# bug = []
# s = 0
# for key, value in new_d.items():
#     if s + key <= 10000:
#         s += key    
#         bug.append(value)
 

# print(bug)


f = open('itog.txt', encoding='utf-8')

s = f.read().lower().replace(',','').replace('.', '').split()

vowels = set('ауеоаыяию')

dict={}

for w in s:
    c= 0
    for v in vowels:
        if v in w:
            c += w.count(v)
    if c == 6:
        dict[w] = {"длина слова" : len(w), "уникальные буквы" : ','.join(sorted(list(set(w)))), "их количество" : len(set(w))}
        
from json import dumps

res = dumps(dict, ensure_ascii=False, indent=4)

print(res)

        