a=5
b=5
#two boxes same value
#and with address
print(id(a))#808

print(id(b))#808
#same address because python optimize memory and store same value in same address
b=6;
print(id(b))#840
k=5;
print(id(k))#808

#garbage collection
#-python garbage collection ka use karta hai memory ko free karne ke liye
b=5;
print(id(b))#808
#so now 6 wala object is free and memory is free for other object

#string interning
name='akash';
name1='akash';
print(id(name))#2250907800736
print(id(name1))#2250907800736

#normal data se internning

a='my fav color is red but i love blue';
b='my fav color is red but i love blue';
print(id(a))#2090477604896
print(id(b))#2090477604896
print(id(a)==id(b))#True