#string #two-pointers
- A palidrome is a word which is the same when we reverse the order its characters (eg. waw, bob)
- Note that we do not consider non alpha-numeric string when constructing a palindrome.
- A simple $O(n)$ solution exists which consist of
	- Filtering out the non alpha-numeric strings in  $O(n)$ 
	- Reversing the word order in  $O(n)$ 
	- Comparing the position of each character in  $O(n)$ 
- However, a better solution exists where we use two pointers to compare both ends of the word in one  $O(n)$  loop.
- In this solution, we initialize a left and right pointer such that the values of these pointers are compared, if they match, the left and right pointer goes closer together by one character (at same time) while skiping non alpha-numeric charaters if they come accross them.

## Pseudo-code
```c
left_pointer = 0
right_pointer = index of last character of word

while left and right points didn't meet:
	push any pointer close to the other when meeting non alphanumeric 
	compare the value of both pointers
```