def solution(inputArray):
    largestProduct = inputArray[0] * inputArray[1]

    i = 0
    j = 1
    while j < len(inputArray):
        if(inputArray[i] * inputArray[j]) > largestProduct:
            largestProduct = inputArray[i] * inputArray[j]

        j += 1
        i += 1

    return largestProduct


if __name__ == "__main__":
    print(solution([3, 6, -2, -5, 7, 3]))
