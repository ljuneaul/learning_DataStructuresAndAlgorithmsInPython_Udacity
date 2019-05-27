"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(a):
    pibotIndex = len(a)-1
    compareIndex = 0
    if len(a) <= 1:
        return a

    while compareIndex < pibotIndex-1:
        # print(a, '   c ', compareIndex, a[compareIndex], '    p ', pibotIndex, a[pibotIndex])

        if a[compareIndex] > a[pibotIndex]:
            (a[pibotIndex-1], a[compareIndex], a[pibotIndex]) = (a[pibotIndex], a[pibotIndex-1], a[compareIndex])
            pibotIndex -= 1
        else:
            compareIndex += 1
    if a[compareIndex] > a[pibotIndex]:
        a[compareIndex], a[pibotIndex] = a[pibotIndex], a[compareIndex]

    # print(a[0:pibotIndex], a[pibotIndex+1:])

    left = quicksort(a[0:pibotIndex])
    right = quicksort(a[pibotIndex:])
    
    a[0:pibotIndex] = left
    a[pibotIndex:] = right
    # print(a)
    return a

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))
print(type(1))