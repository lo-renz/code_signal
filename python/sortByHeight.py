def solution(a):
    index_list = []
    sorted_list = []
    for i in range(len(a)):
        if(a[i] == -1):
            index_list.append(a[i])
        else:
            index_list.append("swap")
            sorted_list.append(a[i])

    slist = sorted(sorted_list)
    
    k = 0
    for j in range(len(index_list)):
        if(index_list[j] == "swap"):
            index_list[j] = slist[k]
            k += 1
    
    return index_list