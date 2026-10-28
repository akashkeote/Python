a=10;
def something():
    a=15;
    print("inside : ",a);
    print("global inside : ",globals()['a'])
    globals()['a']=3333;
something()
print("outside : ",a);