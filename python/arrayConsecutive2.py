def solution(statues):
    # tmp = x
    # x = y
    # y = tmp

    # linear sort
    i = 0
    j = 1
    while i < len(statues):
        if statues[j] < statues[i]:
            tmp = statues[j]
            statues[j] = statues[i]
            statues[i] = tmp
            j += 1
        i += 1

    #return statues

    #re-iterate the list to find out how many statues are needed
    i = 0
    j = 1
    statue_count = 0
    while j < len(statues):
        if statues[j] - statues[i] != 1:
            statues.insert(i+1, statues[i] + 1)
            statue_count += 1
        i += 1
        j += 1

    return statue_count


if __name__ == "__main__":
    print(solution([6, 2, 3, 8]))
