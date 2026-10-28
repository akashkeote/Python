a=input("enter kar be a ")
b=input("enter kar be b ")
print(type(a))#string
print(type(b))#string

a=int(a);
b=int(b);

a,b=b,a
print("a=",a,"b=",b);
print(type(a))#int
print(type(b))#int
print(a+b) # 21   not 3 if a=1,b=2


#using an index
a=input("enter kar be a string ")
print(a[3]) #print 4th character of string        Akash  = s

a=input("enter student first name letter: ")[0];
b=input("enter student roll no: ");
print("first letter of stu name is: ",a," and roll no is ",int(b));