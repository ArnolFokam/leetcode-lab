#stack

- A stack is preferable for this problem as parantheses might enclose other parantheses and this is the approritate data structure to pop out encosed parantheses while allowing the possibility identify outer parantheses.

### Pseudo-code

```c
while len(s) > 0:
	append to stack
	if last two elements are valid pairs (), [] or {}:
		pop the last two elements
```