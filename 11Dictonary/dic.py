data = {0:34,1:35,2:36,3:8}
print(data[2]);
#key and value me hoti hai dictionary
data={'akash':32,'sachin':34,'rohit':36}
print(data['sachin']);
print(data.get('sachin'));
print(data.get('jay')); #agar key nahi milegi to none return karega

data={'akash':32,'sachin':34,'rohit':36,'akash':38} #duplicate key nahi hoti hai dictionary me
print(data['akash']); #last value print karega

#zip - combine values and keys to create dictionary
#it will not work if length of keys and values are not same
#and sath hi dictionary khud se nahi banata hai, hume khud se banana padta hai
#duplicate key nahi hoti hai dictionary me
#it not work duplicate key, it will take last value of that key
keys=['akash','rahul','jay'];
values=[7,0,8];
#dict is inbuilt function in python to create dictionary
dict1=dict(zip(keys,values));
#seq not maintain list me sequence matter
print(dict1);

dict1.pop('akash');#pop del karta hai
print(dict1);
del dict1['jay'];#del bhi del karta hai
print(dict1);

dict1={'js':'vscode','flutter':['android studio','vs code'],'python':{'pycharm':'game','vs code':'spring'}};

print(dict1);
print('\n')
print(dict1['js'])
print(dict1['flutter'][0])
print(dict1['python']['vs code'])