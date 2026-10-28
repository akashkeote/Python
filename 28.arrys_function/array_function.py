import array as a

arr1 = a.array('i',[1,2,3,4,5,6]);

arr1.append(11);
print(arr1);
arr1.reverse();
print(arr1);
arr1.remove(11);


print(arr1);

arr2=arr1;

arr1[2]=999
arr3=a.array(arr1.typecode,arr1.tolist());
print(arr3)
print(arr2)

#memory effiicent with more operation
arr4=a.array(arr1.typecode,(i for i in arr1));
print(arr4)