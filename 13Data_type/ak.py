x=10
print(type(x));
pi=3.14;
print(type(pi));
#COMPLEX NUMBER
c=6+8j
print(type(c));
a=3;
b=6;
c=complex(a,b);
print(c);
print(type(c));

k=int(pi);
print(k);
print(type(k));
k=float(k);
print(k);
print(type(k));

k='akash';
print(type(k));

greater=b>a
print(greater);

greater=b<a;
print(greater);

is_it=True;
print(is_it);
print(type(is_it));

k=int(True);
print(k);
k=int(False);
print(k);
#result
#print(result); #None
result = None
print(result);

l=[1,2,3,4,5];
print(type(l));
t=(1,2,3,4,5);
print(type(t));
s={1,2,3,4,5};
print(type(s));
d={1:2,3:4,5:6};
print(type(d));
r=range(10);
print(r);
print(type(r));

print(list(r));
print(tuple(r));
print(set(r));

#print(dict(r));
print(dict(enumerate(r)));
print(set(range(100,110)));
print(set(range(100,110,2)));

tup=(5,6,7)
print(list(tup));