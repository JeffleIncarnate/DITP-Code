import random

arr = []
i = 0
while i <= 10000:
    arr.append(i)
    i += 1

random.shuffle(arr)

max = arr[0];    

for i in range(0, len(arr)):      
   if(arr[i] > max):    
       max = arr[i];    
           
print("Largest element present in given array: " + str(max));   
