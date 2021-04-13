def list_overlap(list1, list2):
    ret_list = []
    for i in list1:
        if (i in list2) and not (i in ret_list):
            ret_list.append(i)

    return ret_list

if __name__ == '__main__':
    pass