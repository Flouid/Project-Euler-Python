def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)


def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr = swap(arr, i, j)
    arr = swap(arr, i + 1, high)
    return i + 1


# gets the greatest common denominator of two numbers using euclid's method
def gcd(p, q):
    while p != q:
        if p > q:
            p -= q
        else:
            q -= p
    return p


def permute(to_permute, low=0, high=None):
    to_permute = str(to_permute)
    if high is None:
        high = len(to_permute) - 1
    if low == high:
        print(to_permute)
    else:
        for i in range(low, high + 1):
            to_permute = swap(to_permute, low, i)
            permute(to_permute, low + 1, high)
            to_permute = swap(to_permute, low, i)
