# sequence-allignment-dynamic-programming
Sequence allignment problem using dynamic programming

When solving the Sequence Alignment Problem using a combination of Dynamic
Programming and Divide & Conquer, the program divides the string recursively and stores
the values in memory which is then used again as and when needed, making the algorithm
memory efficient.
The subproblem we are solving is finding the mismatch penalty and trying to minimize it.

Nature of the Graph: Memory vs Problem Size (M+N) Nature
--------------------------------------------------------
Basic- Polynomial (O(mn))
Efficient- Linear (O(m + n))

Explanation:
------------
After running the algorithm for 15 different test cases, we have observed that for the
smallest size problem, the memory efficient version (combination of Dynamic Programming
and Divide & Conquer) takes more space as compared to the basic (Dynamic Programming)
solution which is attributed to the memoization feature employed. However, as the problem
size increases the benefit of the memoization is seen. As a result of which, we see a
significant improvement in the memory efficiency of the program.

Nature of the Graph: CPU Time vs Problem Size (M+N):
----------------------------------------------------
Basic- Polynomial (O(mn))
Efficient- Polynomial (O(mn))

Explanation:
------------
The overall computation of the time for both the basic and efficient algorithms are dictated
by the lengths of the strings (m & n). As a result of this, both the algorithms have the same
polynomial time complexity of O(mn). With that being said, the additional computation
involved in the efficient algorithm to implement the memoization functionality is also added
to the time taken to complete execution. This addition although does not deviate the
polynomial time complexity, it still makes the efficient algorithm run for a longer time in
comparison with the basic algorithm as indicated in the above graph. Therefore, the CPU
Time required for the more efficient version is more than that required for the less efficient
version. The difference between the times required by both versions increases as the
problem size increases.
