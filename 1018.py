n,m = input().split(" ")

w_first, b_first = [] , []

chess = []
asd = [["W","B","W","B","W","B","W","B"],["B","W","B","W","B","W","B","W"]]

for i in range(8):
 if i%2==0: 
  w_first.append(asd[0])
  b_first.append(asd[1])
 else:
  w_first.append(asd[1])
  b_first.append(asd[0])

for i in range(int(n)):
  chess.append(input())


cnt = []

for i in range(int(n)-7):
  for j in range(int(m)-7):
    w_cnt = 0
    b_cnt = 0
    for k in range(8):
      for l in range(8):
        if chess[k+i][l+j] != w_first[k][l]:
          w_cnt += 1
        if chess[k+i][l+j] != b_first[k][l]:
          b_cnt +=1
    if w_cnt > b_cnt:
      cnt.append(b_cnt)
    else:
      cnt.append(w_cnt)
print(min(cnt))
  
