import random

# Question 1


def counting_sort(lst, max=100):
    mid_list = [0] * (max + 1)
    sorted_lst = []

    for e in lst:
        mid_list[e] += 1

    for i, e in enumerate(mid_list):
        sorted_lst.extend([i] * e)

    return sorted_lst

# Question 2


def ternary_search(lst, target, start = -1, end = -1):
    start = 0 if start == -1 else start
    end = len(lst) if end == -1 else end
    length = end - start + 1

    if length < 3:
        return linear_search(lst, target)

    third = length // 3
    point1 = start + third
    point2 = point1 + third

    if target < point1:
        return ternary_search(lst, target, start, point1 - 1)
    elif target < point2:
        return ternary_search(lst, target, point1, point2 - 1)
    return ternary_search(lst, target, point2, end)


def linear_search(lst, target):
    for i, e in enumerate(lst):
        if e == target:
            return i
    return -1


# Question 3


def insertion_sort(lst):
    for i in range(1, len(lst)):
        ci = i
        while ci > 0 and lst[ci] < lst[ci - 1]:
            lst[ci], lst[ci - 1] = lst[ci - 1], lst[ci]
            ci -= 1


# Question 4


def nary_search(lst, target, n):
    index = -1

    return index


# Question 5


def jumping_binary_search(sorted_lst, target, jump):
    index = -1

    return index


# This function generates lists of random integers, you can use it to test your sorting code if you wish


def random_list(n=10):
    return [random.randint(0, 100) for i in range(n)]


# This function generates a sorted list of a given size (10 by default). You can use it to test your searching function if you wish


def sorted_list(n=10):
    return sorted(random_list(n))


# Tests

# Q1

print("Testing Q1")
print()

test_list = random_list()
print(test_list)
print(counting_sort(test_list))

print()
print("Q1 Test Done")

# Q2

print()
print("Testing Q2")
print()

test_list = sorted_list()
print(test_list)
print(ternary_search(test_list, test_list[5]))
print(ternary_search(test_list, test_list[6]))
print(ternary_search(test_list, test_list[7]))
print(ternary_search(test_list, test_list[8]))
print(ternary_search(test_list, 0))

print()
print("Q2 Test Done")


# Q3

print()
print("Testing Q3")
print()

test_list = random_list()
print(test_list)
insertion_sort(test_list)
print(test_list)

print()
print("Q3 Test Done")
