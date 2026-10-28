num=5;
#print("One")
#print("Two")
##print("Three")
#print("Four")
#print("Five")

#elif statement
if(num==1):
    print("One");
elif(num==2):
    print("Two");
elif(num==3):
    print("Three");
elif(num==4):
    print("Four");
else:
    print("Five");


score = int(input("Enter a Score: "));
if(score>=90):
    print( "Grade A+");
elif(score>=75 and score<=89):
    print("Grade A");
elif(score>=60 and score<=74):
    print("Grade B");
else:print("Grade C");
