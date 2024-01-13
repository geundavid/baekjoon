today = list(map(int,input().split(" ")))
d_day = list(map(int,input().split(" ")))


days = [31,28,31,30,31,30,31,31,30,31,30,31]

tot = 0
flag = False

if d_day[0] - today[0] > 1000:
  print("gg")
  exit(0)
elif d_day[0] - today[0] == 1000:
  if d_day[1] > today[1]:
    print("gg")
    exit(0)
  elif d_day[1] == today[1]:
    if d_day[2] >= today[2]:  # *d_day[2]랑 today[2]가 같은 경우에도 gg 출력해야되는데
      print("gg")
      exit(0)
      
tot += d_day[2]
d_day[1] -=1
if d_day[1]==0:
  d_day[1]=12
  d_day[0]-=1
  
while 1:
  #print(d_day[0],tot)
#윤년 check
  if((d_day[0]%4==0 and d_day[0]%100!=0) or d_day[0]%400==0):
    days[1]=29     
  else:
    days[1]=28
  #print(d_day[0],tot)
  # *윤년일 때 days[1]+=1해버림


#년도 같아질 때
  if d_day[0]==today[0]:
    
    while d_day[1]>0:
      if d_day[1]==today[1]:
        tot += (days[d_day[1]-1] - today[2]) 
        flag = True
        break
        
      tot += days[d_day[1]-1]
      d_day[1]-=1

  if flag ==True:
    break

 
  while d_day[1]>0:
    print(d_day[1])
    tot+=days[d_day[1]-1]
    d_day[1]-=1
    
    
  d_day[0] -=1
  d_day[1] = 12

print("D-"+str(tot))

