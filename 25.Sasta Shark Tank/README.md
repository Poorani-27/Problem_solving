# Sasta Shark Tank

## Problem Description

Devendra just had a million-dollar idea and he needs funds to startup. He was recently invited to Sasta Shark Tank (A TV show where entrepreneurs pitch their ideas to investors hoping to get investment in return).

He was offered deals from two investors. The first investor offers A dollars for 10% of his company and the second investor offers B dollars for 20% of his company. Devendra will accept the offer from the investor whose valuation of the company is more. Determine which offer will Devendra accept or if both the offers are equally good.

## Input Format

The first line contains a single integer T - the number of test cases. Then the test cases follow.
Each test case contains two integers A and B - the amount offered by first investor for 10% of Devendra's company and the amount offered by second investor for 20% of Devendra's company respectively.

## Output Format

For each test case, Output FIRST if Devendra should accept the first investor's deal, output SECOND if he should accept the second investor's deal, otherwise output ANY if both deals are equally good.

You may print each character of the strings in uppercase or lowercase (for example, the strings "FiRst", "First", "FIRST", and "FIrst" will all be treated as identical).

## Constraints

1 ≤ T ≤ 100
100 ≤ A, B ≤ 10000
A and B are multiples of 100

## Sample Input/Output

### Input
```
3
100 200
200 100
200 500
```

## sample output

```
ANY
FIRST
SECOND
```

## Explanation

- Test case 1: Both investors' valuations of Devendra's company were $1000 since 10% of $1000 = $100 and 20% of $1000 = $200. Therefore, he can accept any of the deals.
- Test case 2: The first investor offered a better deal as he valued Devendra's company at $2000 (since 10% of $2000 = $200) compared to the second investor who valued Devendra's company at $500 (since 20% of $500 = $100).
- Test case 3: The second investor offered a better deal as he valued Devendra's company at $2500 compared to the first investor who valued Devendra's company at $2000.
![](Untitled.png)
![](code.png)