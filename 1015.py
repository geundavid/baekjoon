import copy

n= int(input())

A = list(map(int,input().split(" "))) # map : 요소들을 함수로 처리

comp = copy.deepcopy(A) #A 요소를 comp로 deepcopy
comp.sort() # comp를 내림차순 정렬

ord = []


#print(A)
#print(comp)
for i in range(n):
  for j in range(n):
    if(A[i]==comp[j]):
      ord.append(j)
      comp[j]=-1
      break

ord = list(map(str,ord)) #join 할려면 요소들이 str이어야함
print(" ".join(ord)) # join으로 리스트 합치기, 요소들 공백으로 합침
      


