nums1=65,56,56,56,45,33
print(nums1)

nums2=[45,23,7,68,78,567]
print(nums2)
print(nums2[3])
print(nums2[-3])

#slicing the list
print(nums2[0:2])
print(nums1[0:2])

print(nums2[1:])
print(nums1[:4])


names=['akash','keote']
print(names[1:])

#mix vlaues
namess=['akash','keote',7,1.3]
print(namess)

#list of list
mix=[['akash','keote'],[7,1.3]]
print(mix)
print(mix[1])
print(mix[0][0])

MIX=mix+names
print(MIX)


#append
MIX.append(777)
print(MIX)
#count
print(MIX.count(777))

#insert
MIX.insert(0,'jay')
print(MIX)

#remove
MIX.remove('jay')
print(MIX)

#pop
MIX.pop()
#last value get pop
print(MIX)
#extend
MIX.extend(['jay','keote','mi','ahe'])
print(MIX)

MIX[0:1]=[54,76]
print(MIX)
MIX.reverse()
print(MIX)

MIX.sort
print(MIX)

nums=[4,5,67,8,9]
print(max(nums))
print(sum(nums))
print(min(nums))

#min and max on string allow
#sum not allow

