s = {1,2,3,4,5}
print(s,type(s))



s.add(6)
print(s)




s1 = {10,20,30,40}
s2 = {20,40,50,60}

s3 = s1.union(s2)
print(s3)


s4 = s1.intersection(s2)
print(id(s4))
print(s4)
print(id(s4))



s5 = s1.difference(s2)
print(s5)


s6 = {100,200,300,400}
s7 = {100,200}

print(s7.issubset(s6))
print(s7.issuperset(s6))
print(s6.issuperset(s7))




s8 = {1000,2000,3000}
s9 = {4000,5000}
print(s9.issubset(s8))


s10 = {101,102,103,104,105}
r = s10.pop()
print(s10,r)

s10.remove(103)
print(s10)