# Coloring Words

Cithin is a very artistic person, to the extent that he prioritizes making words on his English essays more colorful over making words that actually make sense. (Maybe that's why he’s failing English.)

Cithin currently has an uncolored word with **N** characters. He can use **C** colors labelled by the numbers **1 ... C**, and he wants to color the word in the sequence of colors represented by **c<sub>1</sub> ... c<sub>N</sub>**. In one operation, Cithin can select a range of characters and color all of it the same color. If the word is currently uncolored, find the minimum number of operations to color the word in Cithin’s desired sequence of colors.

### Input:
The first line will contain 2 integers **N**, **C**. The next line will contain the **N** integers **c<sub>1</sub> ... c<sub>N</sub>**.

### Output:
Print an integer that is the minimum number of operations to color the word in the desired sequence of colors.

### Limits:
- 1 $\le$ **N** $\le$ 10<sup>5</sup>
- 1 $\le$ **C** $\le$ 100
- 1 $\le$ **c<sub>i</sub>** $\le$ **C**

### Limits:
- 2 $\le$ **K** $\le$ **N** $\le$ $10^5$
- 1 $\le$ **x<sub>i</sub>** $\le$ $10^9$

### Example:
**Sample Input:**
```
10 4
1 4 2 1 1 2 4 2 1 3
```

**Sample Output:**
```
6
```
#### Note:
One possible sequence of operations would be:
- $[0, 8]$ &rarr; $1$
- $[2, 7]$ &rarr; $2$
- $[3, 4]$ &rarr; $1$
- $[1, 1]$ &rarr; $4$
- $[6, 6]$ &rarr; $4$
- $[9, 9]$ &rarr; $3$

Problem Author: Avnith Vijayram
