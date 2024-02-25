# Too many Floors

## Problem Description
Chef and Chefina are residing in a hotel with 10 floors, and each floor consists of 10 rooms. Chef's room number is X while Chefina's room number is Y. You need to find the number of floors Chef needs to travel to reach Chefina's room.

## Input Format
- The first line contains an integer T, the number of test cases.
- Each of the next T lines contains two space-separated integers X and Y, the room numbers of Chef and Chefina respectively.

## Output Format
- For each test case, output the number of floors Chef needs to travel to reach Chefina's room.

## Constraints
- 1 ≤ T ≤ 1000
- 1 ≤ X, Y ≤ 100
- X ≠ Y

## Sample Input
```4
1 100
42 50
53 30
81 80
```

## Sample Output

```
9
0
3
1
```

## Explanation
- Test Case 1: Chef needs to climb 9 floors to reach Chefina's room.
- Test Case 2: Chef does not need to climb any floor.
- Test Case 3: Chef needs to go down 3 floors to reach Chefina's room.
- Test Case 4: Chef needs to go down 1 floor to reach Chefina's room.

![](Untitled.png)
![](code.png)