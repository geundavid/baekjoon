n = int(input())

for i in range(n):
  x1,y1,x2,y2 = map(int,input().split())
  m = int(input())
  cnt=0
  for j in range(m):
    x, y, r = map(int, input().split())
    if (x1-x)**2 + (y1-y)**2 <= r**2 and (x2-x)**2 + (y2-y)**2 <= r**2:
      continue
    elif (x1-x)**2 + (y1-y)**2 <= r**2:
      cnt+=1
    elif (x2-x)**2 + (y2-y)**2 <= r**2:
      cnt+=1
     
  print(cnt)
      
