#hashing 
- A bruteforce solution would be to build all possible sequences from the list given and get the longest valid one.
- However, this is computationally expensive as this solution will run in $O(n!)$ time.
- A more effiecient solution would be to sort the list of numbers and therefore, we could loop through the sorted list and count the consecutive sequences.
- This algorithm will run in $O(n \log n)$ 
- Still, there is a more effiecient way of doing this if we can identify the start of every consecutive sequence in the array.
- Notice that the start number of every consecutive sequence is the lowest number of sequence and that if we were to sort numbers, there would gaps between sequences. 

<div style="text-align: center">
<img  src="data:image/png;base64,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"/>
</div>

- Therefore we can loop over the original list to get the start of each sequence and for earch start, we check the length of sequence by look of the consecutive number in the list of numbers given.
- Normally, searching in an array will take $O(n)$ on average but if we use a hash shet we can perform this in $O(1)$ and therefore, our solution would be $O(n)$

## Pseudo-code
```c
starts = []

for n in nums:
	if n - 1  is not in nums:
		add n to starts

max_length = 0

for s in starts:
	length = 1
	while s + length is in nums:
		length += 1
	max_length = max(max_length, length)
	
return max_length
```