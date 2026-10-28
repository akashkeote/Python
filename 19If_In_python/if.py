a=57;
b=55;
x=input("enter a number x: ");
y=input("enter a number y: ");
x=int(x);
y=int(y);
if(x%2==0 and y%2==0):
    print("both are even");
elif(x%2==0&y%2!=0):
    print("x is even and y is odd");
elif(x%2!=0 and y%2==0):
    print("x is odd and y is even");
else:
    print("both are odd");

#4 four spaces indentation is used in python for if else statement
#hinglish - hit karo space 4 times ya phir tab button ka use karo 
if True:
    print("this is true");

    print("AKASH keote");

if False:
    print("this is false");

print("this is not false")
userAge=input("enter your age: ");
userAge=int(userAge);
if (userAge>=18):
    print("you are eligible for voting");
elif(userAge<18 and userAge>0):
    print("you are not eligible for voting");
elif(userAge<=0):
    print("you are not born yet");
