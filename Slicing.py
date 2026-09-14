import array

val = array.array('i', [1, 2, 3, 4, 5])

abc = val[2:5:2]

print(abc)

for i in range(len(abc)):
    print(abc[i], end=" ")
# for reversiing the elements 
ab=val[ : :-1] 
print("Reverse of the array is :",ab)