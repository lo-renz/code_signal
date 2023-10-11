def solution(year):
    if year < 100:
        return 1
    elif year % 10 != 0:
        return (year // 100) + 1
    else:
        return year // 100


if __name__ == "__main__":
    print(solution(10))
    print(solution(99))
