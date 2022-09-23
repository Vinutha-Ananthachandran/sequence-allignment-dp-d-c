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
