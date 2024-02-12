n = int(input())

for i in range(n):
  a = int(input())
  arr = [[1,0],[0,1]]
  for j in range(a-1):
   arr.append([arr[j][0]+arr[j+1][0],arr[j][1]+arr[j+1][1]])

  #print(arr)
  print(arr[a][0],arr[a][1])
    
