# ( )  immutable

tup=[23,34,67,43]
print(tup)
print(type(tup) )
 # type =class  list

 #min value max 
print(max(tup));
print(min(tup));
print(tup.count(67))

#tu-ple is immutable 
#insert and removing method nahi milte hame

print(tup[2])

print(len(tup))

tupA =(2,'akash',7.9)
print(tupA)
num=tupA[0]
#print(num)

num,name,num1=tupA
print(num)
print(name)
print(num1)

#num,name,num1,num2=tupA
#ValueError: not enough values to unpack (expected 4, got 3)

tupB=(34,'akash',[3,4,5,6,7,[1.1]])
print(tupB[2][5][0])
#tupB[1]='jay'
#tupB[0]=[1,2,3,4,5]

tupB[2][1]=7 #this is allow to change
print(tupB[2])

print(1.1 in tupB) #false
print("akash" in tupB) #true
print("Akash" in tupB) #false


tupAk=(50, 40, 90)
x=tupAk[0]
y=tupAk[2]
print(x+y)

tup=(45)
print(type(tup)) #<class 'int'>
tup=(45,)
print(type(tup)) #<class 'tuple'>
