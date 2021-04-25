
arr = list()

while True:
    users = input("Type 'ok' when you are done: ")
    if users == "ok":
        break
    else:
        arr.append(int(users))

n = len(arr)     
# To store the maximum water
# that can be stored
res = 0
     
# For every element of the array
for i in range(1, n - 1) :
      
    # Find the maximum element on its left
    left = arr[i]
    for j in range(i) :
        left = max(left, arr[j])
         
        # Find the maximum element on its right
        right = arr[i]
         
        for j in range(i + 1 , n) :
            right = max(right, arr[j])
             
        # Update the maximum water
res = res + (min(left, right) - arr[i]);
print(res)

