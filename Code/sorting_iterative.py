#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) when everything but the last two items are unordered.
    Memory usage: O(1) Not storing any data"""
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            return False
    return True


def bubble_sort(items, j=0):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running Time: O(n^2), itterates over n items n times
    Memory usage: O(1) not storing any data from items"""
    for i in range(len(items)-1-j):
        if items[i] > items[i+1]:
            items[i], items[i+1] = items[i+1], items[i]
    if j < len(items):
        bubble_sort(items, j+1)


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
