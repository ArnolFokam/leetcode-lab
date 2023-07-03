#1D-DP 
- Iterate over the string of characters
- **if** a word can be found from the beginning of the string to current character, store the break index
- **else** check if a word can be found from the previous breaks. if yes, store the break index
- Return true if the set of saved break index contains the last index of our string of characters
- the time complexity is $O(mn^2)$ , here we assume that hashing a string can be done in $O(n)$ time. This is because we loop the string and for each character $O(n)$, we check from our previous break $O(m)$ if we can form a word through a dictionary check $O(n)$  
- The space complexity is $O(n)$ for case where each can be found in our dictionary. In this case, the number of breaks saved is equal to the number of characters in the string.