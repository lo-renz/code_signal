def solution(sequence):
    first_fail = 0
    second_fail = 0

    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i + 1]:
            first_fail = first_fail + 1

    for i in range(len(sequence) - 2):
        if sequence[i] >= sequence[i + 2]:
            second_fail = second_fail + 1

    return (first_fail < 2) and (second_fail < 2)


if __name__ == "__main__":
    #print(solution([10, 1, 2, 3, 4, 5]))
    print(solution([3, 5, 68, 93, 2]))
