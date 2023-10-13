def solution(a):
    i = 0
    j = 1
    while i < len(a):
        if a[i] == -1:
            i += 1
            j = i + 1
        elif a[i] < a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
        i += 1
    return a


if __name__ == "__main__":
    a = [-1, 150, 190, 170, -1, -1, 160, 180]
    print(solution(a))
