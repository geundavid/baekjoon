n = int(input())

s = []
for i in range(n):
  s.append(input())

s = list(dict.fromkeys(s))

#print(s)

i=len(s)-1
while i>0:
  for j in range(0,i):
    if len(s[j])>len(s[j+1]):
      s[j],s[j+1]=s[j+1],s[j]
    elif len(s[j])==len(s[j+1]):
      if s[j]>s[j+1]:
         s[j],s[j+1]=s[j+1],s[j]
  i-=1

for i in range(len(s)):
  print(s[i])



