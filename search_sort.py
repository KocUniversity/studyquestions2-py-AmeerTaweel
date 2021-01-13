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


def ternary_search(lst, target):
    index = -1

    return index


# Question 3


def insertion_sort(lst):
    sorted_lst = None

    return sorted_lst


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

test_list = random_list()
print(test_list)
print(counting_sort(test_list))

print("Q1 Test Done")
