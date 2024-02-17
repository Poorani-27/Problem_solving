# Is the Score Consistent

Chef is watching a football match and wonders if it's possible for the score to become a certain value at a later point in the game. This program helps Chef by determining whether such a score is possible.

## Input Format

- The first line contains an integer T, the number of test cases.
- For each test case:
  - The first line contains two integers A and B, representing the initial number of goals scored by team 1 and team 2 respectively.
  - The second line contains two integers C and D, representing the final number of goals team 1 and team 2 must score respectively.

## Output Format

For each test case:
- "POSSIBLE" if it's possible for the score to become C:D at a later point in the game.
- "IMPOSSIBLE" otherwise.

You may print each character of POSSIBLE and IMPOSSIBLE in uppercase or lowercase.

## Constraints

- 1 ≤ T ≤ 1000
- 0 ≤ A, B, C, D ≤ 10

## Sample Input

```
3
1 5
3 5 
3 4
2 6
2 2
2 2



```

## sample output
```
POSSIBLE
IMPOSSIBLE
POSSIBLE
```

## Explanation

- Test case 1: The current score is 1:5. If team 1 scores 2 more goals, the score will become 3:5. Thus 3:5 is a possible score.
- Test case 2: The current score is 3:4. It can be proven that no non-negative pair of integers exists such that if team 1 scores x more goals and team 2 scores y more goals the score becomes 2:6 from 3:4. Thus in this case 2:6 is an impossible score.
- Test case 3: The current score is already 2:2. Hence it is a possible score.
