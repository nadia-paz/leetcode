/*
Table: Logs

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column.
 

Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.

*/

-- my solution
WITH temp AS (
    SELECT num,
    LEAD(num, 1) OVER(ORDER BY id) AS num2,
    LEAD(num, 2) OVER(ORDER BY id) AS num3
FROM Logs
)
SELECT DISTINCT num AS ConsecutiveNums
FROM temp
WHERE num = num2 AND num = num3;

-- online solution with self joins
SELECT DISTINCT A.num AS "ConsecutiveNums"
FROM logs A 
JOIN logs B ON A.id = B.id - 1 
JOIN logs C ON B.id = C.id - 1
WHERE A.num = B.num AND A.num = C.num

/* My solution didn't pass the test # 22 out of 23.
 Which is weird, since the problem states AT LEAST three times. 
 The error occurs because id is autoincremental, meaning that somewhere exists id=3
 But it also possible that id 3 was simply removed from the table
Input
Logs =
| id | num |
| -- | --- |
| 1  | 1   |
| 2  | 1   |
| 4  | 1   |
| 5  | 1   |
| 6  | 2   |
| 7  | 1   |

Use Testcase
Output
| consecutivenums |
| --------------- |
| 1               |
Expected
| ConsecutiveNums |
| --------------- |
*/