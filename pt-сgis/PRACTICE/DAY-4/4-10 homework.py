f = open('TXT.TXT', encoding='utf-8')


lst = f.read()

lst = (lst.replace('"','')
       .replace(',','')
       .split())

print(max(lst, key=len))
