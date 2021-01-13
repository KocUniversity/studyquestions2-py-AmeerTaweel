# Algorithmic Complexity

### Free Code

What is the time complexity of the following algorithms? Write a short explanation for each case.

1.

```
a, b = 0, 0
for i in range(N):
  a += a * a

for j in range(M):
  b += b * b;
```

> Time Complexity: O(N + M) or O(N * M)?

Answer:

Time complexity is O(N + M). The first loop is O(N), and the second is O(M), and they are not nested.

2.

```
a = 0
for i in range(N):
  for j in range(N):
    a += i - j
```

> Time Complexity: O(log N) or O(N) or O(N^2) or O(N * log(N))?

Answer:

Time complexity is O(N^2), because there is a nested loop, each of them is O(N).

3.

```
i, j, k = N/2, 2, 0

while i < N:
  while j < N:
    k = k + n / 2;
    j *= 2
  i += 1
```

> Time Complexity: O(log N) or O(N) or O(N^2) or O(N * log(N))?

Answer:

Time complexity is O(N * log(N)) because the outer loop is O(N) and the nested loop is O(log(N)).

4.

```
a, i = 0, N
while i > 0:
  a += i
  i /= 2
```

> Time Complexity: O(log N) or O(N) or O(N^2) or O(N * log(N))?

Answer:

Time complexity is O(log N) because there is only one O(log n) loop.

### Searching

1. What is the cost of searching an element in an unsorted list? Think about best and worst cases? Can you name the algorithmic complexity of the searching algorithm? (Linear, Logarithmic, Quadratic, etc.)

Answer:

Worst case: O(N), Linear
Best case: O(1), Constant

2. Now, assume the list is sorted and we are searching for a value? What can we do to improve the speed of our searching algorithm? Can you find a way to reduce the complexity of the algorithm? Can you name the algorithmic complexity of the *new* searching algorithm?

Answer:

Worst case: O(log N), Logarithmic
Best case: O(1), Constant

3. Now, assume we are searching for the maximum element in the **sorted** list. What is the best way of finding the maximum element in the **sorted** list? Can you name the algorithmic complexity of that search algorithm?

Answer:

The best way is to just return the last element of the list, it will always be the max of it (assuming the list is sorted from least to max).

Worst case: O(1), Constant
Best case: O(1), Constant

### The Devil in the Permutations

Remember the first question of PS3.5 where you wrote a recursive function to find all permutations of a string? What is the time complexity of that function, and why?

Answer:

Time complexity is O(N!) (Factorial), because we loop through all the permutations of length N - 1 O((N - 1)!), then loop through all the N indexes to insert the current character in a nested loop O(N), when we multiply these we get O(N!).

### Math is fun!

Remember the two different ways of computing exponentiation recursively that we have seen earlier in the class. Now that you know complexity classes, can you comment on their complexity, which complexity classes do each belong to?

1.
```
# write a recursive function to compute exponentiation: x**n
# pow(x, n) = x * pow(x, (n-1))
def exponentiate(x, n):
  if(n == 0):
    return 1
  else:
    return x * exponentiate(x, n - 1)
```

Answer:

Complexity is O(N), since we do N multiplications.

2.

```
# if n is even, then x**n = (x**2)**(n/2)
# if n is odd, then x**n = x * (x**2)**((n-1)/2)

def exponentiate_faster(x, n):
  if(n == 0):
    return 1
  else:
    if n % 2 == 0:
      return exponentiate_faster(x**2, n/2)
    else:
      return x * exponentiate_faster(x**2, (n-1)/2)
```

Answer:

Complexity is O(log N), because we reduce the power by half in each call.

### Duplicates

Write a function called `repetitive` which checks for duplicates in a list of integers and returns `True` if there are any duplicates and `False` otherwise. What is the complexity of the algorithm you come up with in your first go? Can you make better than that?

**Hint**: What if I tell you that integers in the list can only take values between 0 and 100 (i.e. some fixed number and I tell you that number)? I also tell you that we have unlimited storage, can you create a *mapping* which will make your life better when searching for repetitive elements?

Answer:

Complexity of first algorithm is O(N^2) because for each number I will loop through the whole list again to check for duplicates.

Improvement: If I know that list can take values between A and B, I'll loop from A to B, and for each value loop through the list and check if it happens more than once. The complexity of this will be O(K * N), but K might be large.

Another Improvement: Using a hash table! Loop through the values, and for each number make a key in the table and for each next number check if the key exists in the table. Complexity is O(N)! This is the kind of improvements we want!

### Random Question

Now, assume you are given two lists and you are asked to find how many elements of the first list is also element of the second list. So, the problem is finding the number of common elements.

> list1 = [1,2,3,4,5]
> list2 = [3,4,5,6,7,8]

In that case, answer should be 3 since 3,4,5 are the common elements.

Implement an algorithm to solve this problem. The most basic way might be checking all elements of the first list whether they are also in the second list. Analyze this algorithm's complexity. If we are given two lists whose lengths are N and M, what should be algorithmic complexity of this solution?

Answer:

Algorithm is easy, will not implement it, but the complexity will be O(N * M) since for each element of list 1 we will loop through all the elements of list 2.

Now, please optimize the algorithm. What can you do improve the speed of the algorithm? Think about the possibilities. For example, lists can be sorted or unsorted.

**Hint**: Every time, we are searching for an element. Can you suggest a better way for this? There is a trade-off between speed and space. What if you construct a database with the second list and query if an element is present instead of searching.

**Hint2**: Asking if an element in a list will require a linear search. Asking if an element in a dictionary will not require any search and it is constant.

Answer:

For the first list, loop through each element and set a key in a dictionary with value: True for it. Then loop through the second list and if the dictionary has a key with that number and is True, add the element to the result list. The complexity of this is O(N + M) which is O(N), assuming N is the length of the longer list.
