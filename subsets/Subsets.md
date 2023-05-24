#backtracking
- Simple backtracking algorithm where at each i = index in the array we branch through two condition
    - include the element at i
    - do not include the element at i
- Base case is when i is greater than all the possible indices of the list of number given
- Space complexity: O(n)
- TIme complexity: O(n*2^n)