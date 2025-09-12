"""

1. Identify the number of rows and columns required.
2. Use nested loops (outer loop for rows, inner loop for columns).
3. Decide what to print (number, character, or symbol).
4. Manage spaces for alignment (important in pyramids/centered patterns).
5. Dry run with small values (like n=3 or n=4) to visualize output.

Q1. Number Increasing Triangle

Pattern:

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5


Instructions:

a. Outer loop for rows (1 to n).
b. Inner loop prints numbers from 1 to row number.



Q2. Number Decreasing Triangle

Pattern:

5 4 3 2 1
5 4 3 2
5 4 3
5 4
5


Instructions:

a. Outer loop decreases row size each time.
b. Inner loop prints numbers in decreasing order.


Q3. Constant Number Triangle

Pattern:

5 5 5 5 5
4 4 4 4
3 3 3
2 2
1


Instructions:

a. Outer loop runs from n down to 1.
b. Inner loop prints same number as row value.


Q4. Left Aligned Decreasing Numbers

Pattern:

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1


Instructions:

a. Outer loop decreases length each row.
b. Inner loop prints numbers starting from 1.


Q5. Repeating Number Pyramid

Pattern:

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5


Instructions:

a. Outer loop for rows.
b. Inner loop prints row number repeatedly.


Q6. Reverse Repeating Numbers

Pattern:

5
4 4
3 3 3
2 2 2 2
1 1 1 1 1


Instructions:

a. Outer loop from n down to 1.
b. Inner loop prints row number repeatedly.


Q7. Reverse Counting Pyramid

Pattern:

5
5 4
5 4 3
5 4 3 2
5 4 3 2 1


Instructions:

a. Outer loop for rows.
b. Inner loop prints decreasing numbers starting from 5.


Q8. Centered Number Pyramid

Pattern:

        1    
      1 2  
    1 2 3
  1 2 3 4
1 2 3 4 5


Instructions:

a. Manage spaces before numbers.
b. Print increasing sequence on each row.


Q9. Centered Repeating Number Pyramid

Pattern:

        1    
      2 2  
    3 3 3
  4 4 4 4
5 5 5 5 5


Instructions:

a. Outer loop for rows.
b. Print spaces for alignment then repeat row number.


Q10. Reverse Number Triangle (Centered)

Pattern:

        1    
      2 1  
    3 2 1
  4 3 2 1
5 4 3 2 1


Instructions:

a. Spaces before numbers.
b. Print numbers in reverse order per row.


Q11. Number Triangle with Reverse Order

Pattern:

1
2 1
3 2 1
4 3 2 1
5 4 3 2 1


Instructions:

a. Outer loop for rows.
b. Inner loop counts down from row number to 1.


Q12. Continuous Numbers

Pattern:

1
2 3
4 5 6
7 8 9 10


Instructions:

a. Maintain a counter variable.
b. Print sequential numbers row-wise.


Q13. Continuous Numbers (Odd Row Expansion)

Pattern:

1
2 3 4
5 6 7 8 9


Instructions:

a. Counter variable increases continuously.
b. Row size grows in odd numbers.


Q14. Multiplication Table Pattern

Pattern:

0
0 1
0 2 4
0 3 6 9
0 4 8 12 16


Instructions:

a. Outer loop for rows.
b. Inner loop prints row*col value.


Q15. Square Numbers Pattern

Pattern:

0
0 1
0 1 4
0 1 4 9
0 1 4 9 16


Instructions:

a. Outer loop for rows.
b. Inner loop prints squares of column index.


Q16. Repeated Square Numbers

Pattern:

1
4 4
9 9 9
16 16 16 16
25 25 25 25 25


Instructions:

a. Outer loop row number squared.
b. Repeat the value as per row index.


Q17. Odd Numbers Triangle

Pattern:

1
3 3
5 5 5
7 7 7 7
9 9 9 9 9


Instructions:

a. Generate odd numbers.
b. Repeat number equal to row count.


Q18. Star Right Triangle

Pattern:

*
* *
* * *
* * * *
* * * * *


Instructions:

a. Outer loop rows.
b. Inner loop prints '*' as per row count.


Q19. Star Inverted Triangle

Pattern:

* * * * *
* * * *
* * *
* *
*


Instructions:

a. Outer loop rows decreasing.
b. Inner loop prints '*' count decreasing.


Q20. Star Pyramid

Pattern:

        *
      * *
    * * *
  * * * *
* * * * *


Instructions:

a. Print spaces for alignment.
b. Print stars equal to row index.


Q21. Square Numbers Grid

Pattern:

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5


Instructions:

a. Outer loop rows.
b. Inner loop prints 1 to n each row.


Q22. Square Repeated Numbers

Pattern:

1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5


Instructions:

a. Outer loop rows.
b. Inner loop prints row number repeatedly.


Q23. Alphabet Pyramid (Increasing)

Pattern:

A
A B
A B C
A B C D
A B C D E


Instructions:

a. Use ASCII values with chr().
b. Print increasing letters each row.


Q24. Alphabet Pyramid (Repeating Letters)

Pattern:

A
B B
C C C
D D D D
E E E E E


Instructions:

a. Row number determines letter.
b. Repeat letter as per row index.


Q25. Butterfly Pattern

Pattern:

*       *
**     **
***   ***
**** ****
*********
**** ****
***   ***
**     **
*       *


Instructions:

a. Print stars on both sides with spaces in between.
b. Maintain symmetry in upper and lower half.
Class comments
"""