def binary_search(sortedlist, x, low=0, high=None):
    if high == None:
        high = len(sortedlist) - 1
    print(f"binary_search: x={x} low={low} high={high}")
    if low > high:
        return -1
    mid = (low + high) // 2
    if x == sortedlist[mid]:
        return mid
    elif x < sortedlist[mid]:
        return binary_search(sortedlist, x, low, mid - 1)
    else:
        return binary_search(sortedlist, x, mid + 1, high)


list1 = [1, 3, 6, 8, 9, 11, 23, 45, 51, 79]
print(binary_search(list1, 47))
# zhengjuns-MacBook-Pro:chapter06 zhengjun$ python3 binary_search.py
# binary_search: x=81 low=0 high=10
# binary_search: x=81 low=6 high=10
# binary_search: x=81 low=9 high=10
# binary_search: x=81 low=10 high=10
# -1
# zhengjuns-MacBook-Pro:chapter06 zhengjun$ python3 binary_search.py
# binary_search: x=11 low=0 high=10
# 5
