
data = []
for i in range(301):
    data.append(int(input()))

print(len(data))

inp = data[0]
temp = []
n =1
c = 2
d =3
while inp != 0 :
    A = data[n]
    B= data[c]
    K= data[d]
    T = A
    if(T<B):
        while T != B :
            if (T % K == 0 ):
                temp.append(T)
                break
            T=T+1
    
    inp = inp - 1
    n = n + 3
    c = c + 3
    d = d + 3
    
print(len(temp))
print(temp)
m=1
for i in temp:
    print("case",m," : ",i)
    m=m+1
   
    
    