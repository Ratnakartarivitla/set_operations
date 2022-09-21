#task-19  set()

#creating set
s = {}
print(type(s))
s={1,2,3,4}
print(type(s))

#add
s.add('kiran')
s.add(0)
#pop
s.pop() # pop deletes the smallest  value in the set
print(s)
#remove
s.remove('kiran')
print(s)
#update
s.update({5,6,7})
print(s)


#set operations

# union
s1 = {1,2,3,4,5,6}
s2 = {4,5,6}
print(s1.union(s2))
#intersection
print(s1.intersection(s2))
#difference
print(s1.difference(s2))
#symmetric
print(s1.symmetric_difference(s2))
#issubset
print(s2.issubset(s1))
#issuperset
print(s1.issuperset(s2))
#isdisjoint
s3={1,2}
s4={4,5}
print(s3.isdisjoint(s4))