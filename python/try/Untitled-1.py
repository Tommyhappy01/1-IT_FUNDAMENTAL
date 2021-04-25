
​
```text
Inputs
------------------------------
Type 'ok' when you are done: 5
Type 'ok' when you are done: 4
Type 'ok' when you are done: 5
Type 'ok' when you are done: ok
​
Output
------
1
​
Inputs
------------------------------
Type 'ok' when you are done: 2
Type 'ok' when you are done: 1
Type 'ok' when you are done: 2
Type 'ok' when you are done: 3
Type 'ok' when you are done: 2
Type 'ok' when you are done: 3
Type 'ok' when you are done: ok
​
Output
------
2
​
Inputs
------------------------------
Type 'ok' when you are done: 6
Type 'ok' when you are done: 5
Type 'ok' when you are done: 8
Type 'ok' when you are done: 9
Type 'ok' when you are done: 2
Type 'ok' when you are done: 4
Type 'ok' when you are done: 3
Type 'ok' when you are done: 6
Type 'ok' when you are done: ok
​
Output
------
10
```
​
### Solution :
​
​
```python
# initialize the list of an integer array representing the elevation, and set it to empty
height = []
# Unless user types `ok`, get input of numbers from the user
while True:
    num = input("Type 'ok' when you are done: ")
    # if the input is not equal to `ok`, add the input number to the height array
    if num != "ok":
        height.append(int(num))
    # if the input equals to `ok`, get out of the while loop
    else:
        break
# initialize areas which holds total amount of water to be trapped, and set to 0
areas = 0
# initialize maximum left and right, and set to 0
max_l = max_r = 0
# initialize left, and set to 0
l = 0
# initialize right and set to the last index of the input array
r = len(height)-1
# unless the current position of the height on left
# is not greater than the one on right, run the loop
while l < r:
    # if the current position on left is lower than the right,
    # max level on left determines the amount of water to be trapped.
    if height[l] < height[r]:
        # if the current height on left is greater than max height on left
        # then the water not to be trapped, and set the max height to the new max
        if height[l] > max_l:
            max_l = height[l]
        # otherwise, add the amount of water to be trapped.
        else:
            areas += max_l - height[l]
        # increase current position on left by one
        l += 1
    # if the current position on left is higher than the right,
    # max level on right determines the amount of water to be trapped.
    else:
        # if the current height on right is greater than max height on height
        # then the water not to be trapped, and set the max height to the new max
        if height[r] > max_r:
            max_r = height[r]
        # otherwise, add the amount of water to be trapped.
        else:
            areas += max_r - height[r]
        # decrease current position on right by one
        r -= 1
# print the amount of water to be trapped
print("\nRain-trapped area : ", areas)
```
​
    Type 'ok' when you are done: 4
    Type 'ok' when you are done: 3
    Type 'ok' when you are done: 6
    Type 'ok' when you are done: 0
    Type 'ok' when you are done: 1
    Type 'ok' when you are done: 0
    Type 'ok' when you are done: 2
    Type 'ok' when you are done: ok
    
    Rain-trapped area :  6
    
​
​
```python
​
```
Collapse

