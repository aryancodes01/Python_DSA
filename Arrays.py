import array
val=array.array('i',[1,2,3,4,5])
for i in val:
  print(i,end=" ")
print("\n")
  # for reversing the elements 
val.reverse()
for x in val:
  print(x,end=" ")
print("\n")
# for inserting value   
val.insert(1,50)
val.append(100)  
print(val)
print("\n")
# for replacing any elemnts by its index 
val[2]= 30
print(val)
copyarray=array.array(val.typecode,(x for x in val))
print(copyarray)