#binary-search
- The main with such problem is to decide when to go left or right
- This is tricky in this situation because we might find our self in portion of the array where we need to go left although we would go right in the baseline binary search implementation and vice versa (due to the rotated array)
- The trick is to identify such situation and account for them in our programming of the binary search algorithm
- A tip is to idenity if we are in the left portion or the right portion of the array and from there, decide which condition makes it better to go left or go right.