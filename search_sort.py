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


def nary_search(lst, target, n, start = -1, end = -1):
    start = 0 if start == -1 else start
    end = (len(lst) - 1) if end == -1 else end
    length = end - start + 1

    if length < n:
        return linear_search(lst, target)

    nth = length // n
    points = [start]
    for i in range(1, n):
        points.append(start + i * nth)
    points.append(end)

    for point in points:
        if point == 0:
            continue
        if target == lst[point]:
            return point
        elif target < lst[point]:
            return nary_search(lst, target, n, points[i - 1], point - 1)

    return -1


# Question 5


def jumping_binary_search(sorted_lst, target, jump):
    i = 0

    while sorted_lst[i] < target:
        i += jump
        if i >= len(sorted_lst):
            i = len(sorted_lst) - 1
            break

    start = (i - jump) if i > 0 else 0
    end = i

    # I'm too lazy to implement binary search in a new method.
    return nary_search(sorted_lst, target, 2, start, end)


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

# Q4

print()
print("Testing Q4")
print()

test_list = sorted_list(50)
print(test_list)
print(ternary_search(test_list, test_list[5], 10))
print(ternary_search(test_list, test_list[6], 10))
print(ternary_search(test_list, test_list[11], 10))
print(ternary_search(test_list, test_list[12], 10))
print(ternary_search(test_list, test_list[49], 10))
print(ternary_search(test_list, test_list[0], 10))
print(ternary_search(test_list, 0, 10))

print()
print("Q4 Test Done")

# Q5

print()
print("Testing Q5")
print()

test_list = sorted_list(50)
print(test_list)
print(jumping_binary_search(test_list, test_list[5], 10))
print(jumping_binary_search(test_list, test_list[17], 10))
print(jumping_binary_search(test_list, test_list[18], 10))
print(jumping_binary_search(test_list, test_list[31], 10))
print(jumping_binary_search(test_list, test_list[49], 10))
print(jumping_binary_search(test_list, test_list[0], 10))
print(jumping_binary_search(test_list, 0, 10))

print()
print("Q5 Test Done")
