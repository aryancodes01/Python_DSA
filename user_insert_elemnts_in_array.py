from array import*
arr=array('i',[])
n=int(input("HOW MANY NUMBERS YOU WANT TO ENTER:"))
for x in range(0,n):
  arr.append(int(input("Enter next number:")))
#for y in arr:
  #print(arr,end=" ")  
i=arr.index(3)  
print(i)
  