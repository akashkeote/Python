def add(num1,num2):
    return num1+num2;

print(add(6,7));
#defualt arguments
def add1(num1,num2=7):
    return num1+num2;

print(add1(6));

#variable lengtrh argument

def add2(num1,*num2):
    print(num1);
    print(num2); #tuple it is
    sum=num1;
    for i in num2:
        sum+=i;
    return sum;

print(add2(6,5,6,7));


def person(name,age=18):
    print("name ",name);
    print("age ",age);

person("akash",22)
person(22,"akash")
#keyword argument
person(age=22,name="akash")




def person(name,**age):
    print("name ",name);
    # print("age ",age);
    for k,v in age.items():
        print("key: ",k,":","value: ",v);

# keyword length  agument
person(name="jay",age=22,loc="pune",tech="python");

