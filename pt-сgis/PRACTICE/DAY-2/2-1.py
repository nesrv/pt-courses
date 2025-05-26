s =  "  ,!. hello pytлon   ..!,  "

# start: stop: step
# print(s[0:5:2])
# print(s[::2])
# print(s[::-1])
# print(s[:5:-1])
# print(s[4:0:-1])

# s[0] = 'H'
# s = 'H' + s[1:]
s = s.capitalize()
print(s)
s = s.upper()
print(s)
s = s.lower()
print(s)
s = s.replace('l', 'л', 1)
print(s)
print(s.find('л'))
print(s.rfind('л'))
s = s.strip()
print(s)
s = s.strip('.!, ')
print(s)

