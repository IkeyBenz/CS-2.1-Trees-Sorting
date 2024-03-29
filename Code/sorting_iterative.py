#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) when everything but the last two items are unordered.
    Memory usage: O(1) Not storing any data"""
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running Time: O(n^2), itterates over n items n times
    Memory usage: O(1) not storing any data from items"""
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running Time: O(n^2), itterates over n items n times
    Memory usage: O(1), not storing any data from items"""
    for i in range(len(items)-1):
        min_index = i
        for j in range(i+1, len(items)):
            if items[min_index] > items[j]:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n^2), itterates over n items n times
    Memory usage: O(1), not storing any data from items"""
    for i in range(1, len(items)):
        curr = items[i]

        j = i-1
        while j >= 0 and items[j] > curr:
            items[j+1] = items[j]
            j -= 1

        items[j+1] = curr
