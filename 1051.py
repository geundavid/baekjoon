n,m = map(int,input().split(" "))

a = []

for i in range(n):
  c = []
  b = int(input())
  j = m-1
  while j > 0:
    if j==1:
      c.append(int(b/10**j))
      c.append(int(b%10**j))
      #print(c)
      a.append(c)
      break
    else:
      c.append(int(b/10**j))
      b = b - int(b/10**j)*10**j
    j-=1
max = 1

#print(a)
for i in range(n):
  for j in range(m):
    k=1
    while k < n-i and k < m-j:
      if a[i][j] == a[i][j+k] == a[i+k][j] == a[i+k][j+k]:
       # print( a[i][j],a[i][j+k] ,a[i+k][j] ,a[i+k][j+k])
        if max < (k+1)**2:
          max = (k+1)**2
      k+=1

print(max)

          
         
         
