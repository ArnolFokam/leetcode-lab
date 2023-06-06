#backtraking
- base case: the partition pivot is at the end of the string. (append the subset used so far)
- branches: inserting the pivot in each possible location of the string we should still consider if the left side of the pivot forms a palindrome