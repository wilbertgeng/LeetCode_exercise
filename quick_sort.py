def quickSort(data_list):
    quickSortHelp(data_list, 0, len(data_list)-1)

def quickSortHelp(data_list, start, end):
    if start < end:
        split_pos = partition(data_list, start, end)
        quickSortHelp(data_list, start, split_pos-1)
        quickSortHelp(data_list, split_pos+1, end)

def partition(data_list, l, pivot):
    low = l
    while l < pivot:
        if data_list[l] < data_list[pivot]:
            data_list[l], data_list[low] = data_list[low], data_list[l]
            low += 1
        l += 1

    data_list[low], data_list[pivot] = data_list[pivot], data_list[low]

    return low

data_list = [54,26,93,17,77,31,44,55,20]
quickSort(data_list)
print(data_list)
