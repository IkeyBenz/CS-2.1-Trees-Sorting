#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n + m) iterates over every elem in items1 and items2
    Memory usage: O(n + m) creates a new list containing elems from items1 and items2"""

    merged = []
    i, j = 0, 0
    while i < len(items1) and j < len(items2):
        if items1[i] < items2[j]:
            merged.append(items1[i])
            i += 1
        else:
            merged.append(items2[j])
            j += 1

    return merged + items1[i:] + items2[j:]



def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: O(nLog(n)) - the cost of sorting
    Memory usage:  O(n) - storing new lists of elements"""
    mid = len(items) // 2
    first, second = items[:mid], items[mid:]
    return merge(sorted(first), sorted(second))


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(nLog(n)) - merge() takes time to run for each iteration
    Memory usage: O(n)* - *although technically there is a recursive stack underneath"""

    if len(items) == 1:
        return items

    mid = len(items) // 2
    return merge(merge_sort(items[:mid]), merge_sort(items[mid:]))

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (the first element) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: O(nLog(n)) but n^2 in worst case?
    Memory usage: O(1) because the swaps happen in place"""
    # Choose a pivot any way and document your method in docstring above
    p = items[low]
    p_index = low + 1
    # Loop through all items in range [low...high]
    for i in range(low + 1, high):
        # Move items less than pivot into front of range [low...p-1]
        if items[i] < p:
            items[i], items[p_index] = items[p_index], items[i]
            p_index += 1

    # Move pivot item into final position [p] and return index p
    items[low], items[p_index-1] = items[p_index-1], items[low]
    return p_index - 1

def quick_sort(items, low=0, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    if high is None:
        high = len(items)

    if high - low <= 1:
        return items

    p_index = partition(items, low, high)

    quick_sort(items, low, p_index)
    quick_sort(items, p_index + 1, high)
    

if __name__ == '__main__':
    from random import randint
    lst = [randint(0, 100) for _ in range(100)]
    reg = sorted(lst)
    quick_sort(lst)
    print(lst)
    print(lst == reg)