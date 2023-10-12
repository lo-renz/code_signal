def solution(sequence):
    # A list of length 1 is considered strictly increasing.
    if len(sequence) == 1:
        return True

    # While loop to find first instance of left number greater than right.
    # Traversing left to right.
    # [1, 2, 3, 4, 3, 6]
    # [0, 1, 2, 3, 4, 5]
    # i = 3

    # [10, 1, 2, 3, 4, 5]
    # [0, 1, 2, 3, 4, 5]
    # i = 0
    i = 0
    while sequence[i] < sequence[i+1]:
        i += 1

    # Traversing right to left
    # [1, 2, 3, 4, 3, 6]
    # [0, 1, 2, 3, 4, 5]
    # j = 4

    # [10, 1, 2, 3, 4, 5]
    # [0, 1, 2, 3, 4, 5]
    # j = 1
    j = len(sequence) - 1
    while sequence[j] > sequence[j-1]:
        j -= 1

    # When the first instance is found, remove it from the list.
    if j > i:
        if sequence[j] < sequence[j-1]:
            sequence.pop(j-1)
        else:
            sequence.pop(j)
    else:
        sequence.pop(i)

    return sequence

    # Loop through the list again to check if there is another instance where the right number is less than the left.
    # [1, 2, 3, 4, 6]
    j = 1
    while j < len(sequence):
        if sequence[j] == sequence[j-1]:
            return False
        elif sequence[j] < sequence[j-1]:
            return False
        j += 1

    return True




if __name__ == "__main__":
    print(solution([10, 1, 2, 3, 4, 5]))
    #print(solution([3, 5, 67, 98, 3]))