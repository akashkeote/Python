#more memory and less cpu power then this one
a=5
b=6
print("Before swapping: a =",    a   ,   "b =",b)
temp = a;
a=b
b=temp;
print("After swapping: a =",    a   ,   "b =",b)

#mathematical way  not using extra memmory but operation jyada hore
#less memory better cpu power
a=10;
b=20;
a=a+b; #30
b=a-b; #30-20 = 10
a=a-b; #30-10 = 20
print("a == ",a,"b ==",b)



#xor
a=a^b;
b=b^a;
a=a^b;
print("a == ",a,"b ==",b)

#inbuilt function to swap two numbers
#tuple packing and unpacking 
a=555555
b=666666
print("Before swapping: a =",    a   ,   "b =",b)
a,b=b,a;
print("After swapping: a =",    a   ,   "b =",b)



#string swappinh
str1="akash"
str2="jay"
str1,str2=str2,str1
print("After swapping: str1 =",    str1   ,   "str2 =",str2)