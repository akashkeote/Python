'akash'
print('akash')
#>>> 'akash'
#'akash'
#>>> print('akash')
#akash

#print('akash's keote')
#error dega ye

print("akash keote")
print('akash\'s "keote"')

print('akash ' 'keote ')
#print karna hai 10 times to ye karo
print('akash ' 'keote |' *10)

#error dega ye
#print('c:\users\navin')
#unicode wala 
print('c:\\users\\navin')


#more on strings 
name = "akash"
print(name+' keote')
print(name[4]) #h

#even h = -1  s=-2 a=-3 k=-4 a=-5
print(name[-1]) #h


#substring
print(name[3:10])
#ye bhi kam karega 
#but jo nahi hai us range 
#me wo skip 5 6 7 8 9 10
print(name[0:3])
print(name[1:]) #1 se 4idx
print(name[:4]) #0 se 3idx tak


#error dega ye 
#print(name[0,3]='AKA')

name="AKASH"
print(name)

print(len(name))

print('\n')
#with eascape seq
name =' hey my name is ,\n akash'
print(name+'\n')

name="""My name is akash
i am the one 
who is going to market"""
print(name)