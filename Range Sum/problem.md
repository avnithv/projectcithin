# Range Sum

Cithin is poor at money management, and for most of his life he has been broke. However, after doing some services that pay quite well, he now has a tangible amount of money and would like to keep it safe. After watching a YouTube tutorial on how to evade tax laws, he realizes he must immediately separate his assets into multiple bank accounts in a certain way.

Cithin has **N** assets, each with a distinct price **x<sub>1</sub> ... x<sub>N</sub>**. He must separate assets into **K** bank accounts such that the sum of the ranges of his bank accounts are minimized. 

The range of a bank account is the difference in the prices of the most and the least valuable assets in that account. An account can also be empty, in which case the range would be $0$.

Cithin needs your help to find the best way to separate his assets depending on the method he chooses. If there are multiple ways, find any one of them.

### Input:
The first line contains two integers **N**, **K**. The next line contains **N** integers **x<sub>1</sub> ... x<sub>N</sub>**.

### Output:
Print **K** lines, where each line contains some integers separated by spaces representing of the prices of the assets in the bank account. If an account has no assets, print $-1$.

### Limits:
- 2 $\le$ **K** $\le$ **N** $\le$ $10^5$
- 1 $\le$ **x<sub>i</sub>** $\le$ $10^9$

### Example:
**Sample Input:**
```
6 3
2 13 8 4 7 1
```
**Sample Output:**
```
13
2 4 1
8 7
```
#### Note:
In the first testcase, the groups have ranges of $0$, $3$, and $1$, which sums to $4$. It can be shown that this is the minimum sum of ranges.

Problem Author: Avnith Vijayram
