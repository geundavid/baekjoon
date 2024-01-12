s = input()

l = []

for i in range(1,len(s)):
  for j in range(i+1,len(s)):
    str1 = list(s[0:i])
    str1.reverse()
    s1 = ''.join(str1)
    
    str2 = list(s[i:j])
    str2.reverse()
    s2 = ''.join(str2)
    
    str3 = list(s[j:])
    str3.reverse()
    s3 = ''.join(str3)
    str = s1 + s2 + s3
    l.append(str)
    
l.sort()
print(l[0])
  
# 1. sort()로 사전순 정리 가능
# 2. reverse()로 순서 뒤집기 가능
# 3. ''.join로 리스트를 문자열로 바꿈

