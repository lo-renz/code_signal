def solution(n):
    # [1, 2, 3, 0]
    n = [int(digit) for digit in str(n)]
    return sum(n[:len(n)//2]) == sum(n[len(n)//2:])


if __name__ == "__main__":
    print(solution(1230))
