def solution(statues):
    statues = sorted(statues)
#        if statues[j] - statues[i] != 1:
#            statues.insert(i, statues[i]+1)

    statue_count = 0
    i = 0
    j = 1
    while j < len(statues):
        if statues[j] - statues[i] != 1:
            statues.insert(i+1, statues[i]+1)
            statue_count += 1
        i += 1
        j += 1

    return statue_count


if __name__ == "__main__":
    print(solution([2, 1]))
