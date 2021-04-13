def list_overlap(list1, list2):
    ret_list = []
    for i in list1:
        if (i in list2) and not (i in ret_list):
            ret_list.append(i)

    return ret_list


if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(list_overlap(a, b))
