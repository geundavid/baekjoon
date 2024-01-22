n, a, b = input().split(" ")

n = int(n)
a = int(a)
b = int(b)

rnd = 0
while int(n)>1:
  n = n/2
  a = a/2 + 0.1 
  b = b/2 + 0.1
#  print(n, a, b)
  if n%2!=0:
    n+=0.5
  rnd +=1
  a = round(a,0)
  b = round(b,0)

  if a==b:
    print(rnd)
    break
