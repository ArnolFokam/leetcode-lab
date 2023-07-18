#graph
- This is the same problem as [[Course Schedule]]
- The only difference is that we need to sorted the "can complete" course as they are encountered
- To prevent the addition of a course more than two times because it is the prerequisite of two course, add the inserted course in another set of course that are inserted
- If a course is found in this set, then this means it was previously visited and we could complete this course so skip the iteration for this course
- Time complexity is $O(V + E)$ and space is $O(V)$.