#graph
- Use hashmap to store "users to tweets" and "users to followee"
- If you want to get the 10 most recent tweets
    - Get a list of tweets for each person you are following
    - Use the **merge K-sorted algorithm** to get the top-10
        1. Set a pointer ot the end of each list
        2. Add all element pointed to a max heap
        3. Set the point to the next element to the left until the pointer points to index -1 for all lists

    - However, we just need to do 2. and 3. 10 most recent times


- The time complexity for get_most_recent is O(k) where k is the number of followee for the user
The space complexity of the algorithm is linear polynimial we respect to the users (since they can follow)