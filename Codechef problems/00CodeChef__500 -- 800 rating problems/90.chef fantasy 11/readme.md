# Chef Fantasy 11

Chef wants to join his friends in playing fantasy cricket based on the ODI World Cup. For each match, he needs to choose a team of 11 players and decide who will be the captain and who will be the vice-captain.

## Problem Statement

Chef needs to select a captain and a vice-captain from his team of 11 players. However, he's only considering a subset of these players for these roles. Given the number of players he's considering (N), determine the number of possible choices for captain and vice-captain.

### Input Format

The input consists of T test cases. The first line of each test case contains a single integer T, denoting the number of test cases. The following lines contain a single integer N, representing the number of players Chef is considering.

### Output Format

For each test case, output the number of possible choices of captain and vice-captain on a new line.

### Constraints

1 ≤ T ≤ 10
2 ≤ N ≤ 11



## sample Input
```
2
2
3

```
## sample output
```
2
6

```

### Explanation

Test case 1: With N=2, there are only two possibilities: one of the players must be selected as the captain, and the other will become the vice-captain.

Test case 2: It can be shown that there are 6 possibilities in total for captain/vice-captain choices.
![](Untitled.png)
![](code.png)
