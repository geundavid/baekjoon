x = int(input())

res = []
i=1
flag = False
while i>0:
  for j in range(0,i):
    if i%2==0:
      res = [1+j,i-j]
      x-=1
      if x==0:
        flag = True
        break
    else:
      res = [i-j,1+j]
      x-=1
      if x==0:
        flag = True
        break
  if flag:
    break
  i+=1
  

print(str(res[0])+"/"+str(res[1]))
