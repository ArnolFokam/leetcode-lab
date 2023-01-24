#array #two-pointers 
- The problem has similar configuration as the [[Two Sum]]. However, a slight modification in our input enables us to produce a more effiecient solution.
- The list of numbers given for this problem are sorted in non-decreasing order.
- As a results, all number on the right will be greater that number in the left and vice versa.
- This means that if we take the sum of two numbers and they are greater than the target, then, we must choose another set of number whose sum is less than the previous one.
- The same is true for a number less than the target and the need to find a set which gives a greater sum.
- If we consider this sequence of numbers while starting at the extreme of the list of numbers.

```c
left -> num1 < nums2 < nums3 < nums4 < nums5 <- right
```

- We will be forming a sum of the smallest and the biggest number in the array
- Therefore, if the result gives us a **smaller** number compared to the target, the only way to get a **bigger** number will be to more the **left** pointer to the **right**.
- Also, if the result gives us a **bigger** number compared to the target, the only way to get a **smaller** number will be to more the **right** pointer to the **left**.
- In this way, we are sure to go over all possible sums effiecienlty while minizing the occurence of undesireable sums and without an additional data structure the other solution.