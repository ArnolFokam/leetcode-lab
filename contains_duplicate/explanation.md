#array #hashing
- A trivial solution would be to use an $O(n^2)$ algorithm that checks if there exists another element in the array for each element traversed in a foor loop.
- However, we can be more computationally effiecient by using a secondary data structure that permits us to rapidly access an element provided we know its value.
- Such data structure could implement a hashing functionaly where for each element inserted in this data struture, we can check whether the element is already present in $O(1)$.
- While we can use a dictionary (python) for that, a set is a better solution since we only need to store the value of the element.

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

Since hash-supported data structures does not allow duplicates. This number of elements of the second data structure will be less than or equal to the number of elements of the original one if there is any diplucate. This is because the the duplicates will have the same hash value and therefore, one will overide the other. As a result, we can reduce our solution to,

```c 
ds2 = initialize secondary data structure with hashing
add all elements in 'numbers' into 'ds2'
return length of 'ds2' is not equal to length of 'numbers'
```