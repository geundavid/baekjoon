n = input()

for i in range(int(n)):
  x1, y1, r1, x2, y2, r2 = map(int, input().split(" "))
  d = (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5
  if d == 0:
    if r1 == r2:
      print(-1)
    else:
      print(0)
  elif d==r1+r2:
    print(1)
  else:
    if d<r1+r2:
      if d == abs(r1-r2):
        print(1)
      elif d < abs(r1-r2):
        print(0)
      else:
        print(2)
    else:
      print(0)

