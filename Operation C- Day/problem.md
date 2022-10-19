# Operation C- Day

Cithin the army commander is planning an attack against the enemy city of Lopital. He has a cool name for it already, _Operation C- Day_, named after his grade in math. However he needs your assistance to choose the best day to launch the attack. 

Lopital has a rotation system for its military with its allies. In particular, it has **N** divisions of the military where the **i**-th division is rotated between cities every **x<sub>i</sub>** days. Let us call a day where all of the divisions are being rotated an _A Day_, named after Lopital’s grade in math. Cithin in his infinite knowledge has determined that if _Operation C- Day_ occurs on an _A Day_, his army will win.

It just so happens that yesterday was such an _A Day_. Cithin is furious at having missed out on such an opportunity. He asks you to find how many days there will be between today and the next _A Day_, inclusive. Since the answer may be large, give the answer modulo $10^9 + 7$.

### Input:
The first line of the input will be an integer **Q**, the number of queries. The first line of each query will contain the integer **N**. The next line will contain **N** integers **x<sub>1</sub> ... x<sub>N</sub>** separated by spaces. 

### Output:
Print **Q** lines, where the with each line containing the number of days between today and the next _A Day_ for a query. Print all answers modulo $10^9 + 7$.

### Limits:
- 1 $\le$ **Q** $\le$ $1000$
- 1 $\le$ **N** $\le$ $100$
- 1 $\le$ **x<sub>i</sub>** $\le$ $10^9 + 7$

### Example:
**Sample Input**
```
3
2
3 5
3
2 4 5
5
1 3 5 6 10
```
**Sample Output:**
```
15
20
60
```
Make sure to print answers modulo $10^9 + 7$

Problem Author: Avnith Vijayram
