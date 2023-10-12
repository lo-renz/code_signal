def solution(inputArray):
    longest_length = 0
    longest_strings = []

    # Grabbing the length of the longest string in the array.
    for arr in inputArray:
        if len(arr) > longest_length:
            longest_length = len(arr)

    # Iterating through the array to add the string with the length equal to longest_length.
    for arr in inputArray:
        if len(arr) == longest_length:
            longest_strings.append(arr)

    return longest_strings


if __name__ == "__main__":
    print(solution(["aba", "aa", "ad", "vcd", "aba"]))