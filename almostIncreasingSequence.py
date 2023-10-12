def solution(sequence):
    # A list of length 1 is considered strictly increasing.
    if len(sequence) == 1:
        return True

    # While loop to find first instance of left number greater than right.
    # Traversing left to right.
    i = 0
    while sequence[i+1] > sequence[i]:
        i += 1

    # [3, 5, 67, 98, 3]
    # [0, 1, 2, 3, 4, 5]
    # Traversing right to left
    #i = len(sequence) - 1
    #while sequence[i] > sequence[i-1]:
    #    i -= 1
    #return i

    # When the first instance is found, remove it from the list.
    sequence.pop(i)
    #return sequence

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
    print(solution([1, 2, 3, 4, 3, 6]))
    #print(solution([3, 5, 67, 98, 3]))