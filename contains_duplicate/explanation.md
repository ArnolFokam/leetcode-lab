#array #hashing
- A trivial solution would be to use an $O(n^2)$ algorithm that checks if there exists another element in the array for each element traversed in a foor loop.
- However, we can be more computationally effiecient by using a secondary data structure that permits use to rapidly access an element provided we know its value.
- Such data structure must implement a hashing functionaly where for each element insert in this data struture, we can check whether the element exsists in $O(n)$.
- There we can use a dictionary in python, but a set is also a solution and better one since we only need to store the value of the element.

## Pseudo-code

```c
ds2 = initialize secondary data structure with hashing

for n in 'numbers':
	if n not in 'ds2':
		add n to 'ds2'
	else:
		return True # duplicate found

return False # duplicate not found
```

## Note

Since hash-supporting data structure does not allow duplicates. This means that the length of the second data structure will be less than equal to the length of the original if there is any diplucate as they will result to the same hash value. Therefore, we can reduce our solution to,

```c 
ds2 = initialize secondary data structure with hashing
add all elements in 'numbers' into 'ds2'
return length of 'ds2' is not equal to length of 'numbers'
```