def solution(inputString):
    return inputString == inputString[::-1]


if __name__ == "__main__":
    print(solution("level"))
    print(solution("name"))
