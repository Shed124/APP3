def merge(list1, list2, key):
    list_merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if smart_cast(list1[i][key]) < smart_cast(list2[j][key]):
            list_merged.append(list1[i])
            i += 1
        else:
            list_merged.append(list2[j])
            j += 1
    while i < len(list1):
        list_merged.append(list1[i])
        i += 1
    while j < len(list2):
        list_merged.append(list2[j])
        j += 1
    return list_merged


def merge_sort(input_list, key):
    if len(input_list) < 2:
        return input_list[:]
    else:
        middle = len(input_list) // 2
        list1 = merge_sort(input_list[:middle], key)
        list2 = merge_sort(input_list[middle:], key)
        return merge(list1, list2, key)
    
def smart_cast(value):
    try:
        return int(value)
    except ValueError:
        return value
