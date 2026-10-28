#sequence

#collection of values 
#collection of unique ele,ent
#unorder unique element ka collection

set1 = {23,56,78,21,56}
print(set1) #56 21 78 23 
#random order aaya bro 

#hashing 
print(23 in set1)
print(len(set1)) #count not work 
print(type(set1)) #<class 'set'>

set2={}
print(set2)
print(type(set2)) #<class 'dict'>
set2=set()
print(type(set2)) #<class 'set'>

set2=set('abcdefgh')
set3=set("xyzwpqmnabcde")
print(set2) #{'g', 'e', 'b', 'f', 'd', 'a', 'h', 'c'}
print(set3) #{'e', 'b', 'x', 'y', 'n', 'w', 'd', 'm', 'z', 'p', 'a', 'c', 'q'}
print(set2-set3) #{'h', 'g', 'f'}
print(set3-set2) #{'x', 'y', 'n', 'w', 'm', 'z', 'p', 'q'}
print(set2|set3) #{'h', 'c', 'q', 'p', 'd', 'y', 'x', 'b', 'f', 'm', 'w', 'e', 'a', 'g', 'n', 'z'}

print(set2&set3) #common one 

print(set2^set3) #{'w', 'p', 'q', 'n', 'g', 'z', 'h', 'f', 'y', 'x', 'm'}

a=set('python')
b=set('telusko')

#{'t', 'o'}
print(a&b) 