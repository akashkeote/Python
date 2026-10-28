#inbuilt array
import array as a

arr1 = a.array('b',[1, 2, 3, 4, 5])
print(arr1.buffer_info)
print(arr1)
print(type(arr1))
for i in arr1:
    print(i)
print(arr1.tolist())



arr2 = a.array('d',[2.5,4.8,-3.2,6.7])
for i in arr2:
    if(i<0):continue;
    print(i)

