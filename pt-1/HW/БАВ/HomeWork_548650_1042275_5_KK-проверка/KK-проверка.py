s='6011 5564 4857 8945 8'

s=list(s.replace(" ",''))
s.reverse()
s3= sum(int(s[i]) for i in range(0,len(s),2))
s2 = [int(s[i])*2 for i in range(1,len(s),2) ]
s2="".join(map(str,s2))
s2=sum((map(int,s2)))

print ('Да' if (s2+s3)%10==0 else 'Нет')

