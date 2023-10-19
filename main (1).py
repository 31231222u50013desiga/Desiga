def linearSearch(arr,value):
   left=0
   right=len(arr)-1
   while(left<=right):
      if(arr[left]==value):
         return left
      elif(arr[right]==value):
         return right
      left+=1
      right-=1
   return -1
array=[1,2,3,4,5,6,7,8,9,10]
value=10
a=linearSearch(array,value)
if(a==-1):
   print("Element not present")
else:
   print("Element present at index",a)