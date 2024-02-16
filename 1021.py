n, m = map(int, input().split(" "))

a = []
b = []
a = list(map(int, input().split(" "))) #map(적용할 함수, 적용할 값)

for i in range(n):
  b.append(i+1)
  
#print(a)
#print(b)
cnt = 0


for i in range(m):
   if len(b) - b.index(a[i]) > (len(b)+1)/2: #해당 원소의 위치가 왼쪽에 치우져있을 때
     for j in range(b.index(a[i])): #해당 원소 전까지 뒤로 보냄
       b.append(b.pop(0))  
       cnt+=1
     b.pop(0) #해당 원소 제거
   elif len(b) - b.index(a[i]) < (len(b)+1)/2: #원소의 위치가 오른쪽에 치우쳐있을때
     for j in range(len(b)-b.index(a[i])): 
       b.insert(0, b.pop(len(b)-1))
       cnt+=1
     b.pop(0)
   else: #원소가 정가운데 위치
     for j in range(b.index(a[i])):
       b.append(b.pop(0))  
       cnt+=1
     b.pop(0)
   #print(b)
print(cnt)
#print(b)
