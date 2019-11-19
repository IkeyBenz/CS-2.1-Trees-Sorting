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
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
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

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

    

if __name__ == '__main__':
    from random import randint
    lst = [randint(0, 100) for _ in range(100)]
    print(merge_sort(lst) == sorted(lst))