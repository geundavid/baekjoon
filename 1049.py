n, a = input().split(" ")

n = int(n)
six = []
one = []

res = 0

for i in range(int(a)):
  
  b , c = input().split(" ")
  six.append(b)
  one.append(c)
  


six = list(map(int,six))
one = list(map(int,one))

six.sort()  # int형 리스트로 만들어준 후에 sort해야함
one.sort() 

#print(six)
#print(one)
while n!=0:
  if n>=6:
    if six[0] > 6*one[0]:
     res += 6*one[0]
    else:
     res += six[0]
    n-=6
  else:
    if six[0] > n*one[0]:
      res += n*one[0]
    else:
      res += six[0]
    n=0

print(res)
