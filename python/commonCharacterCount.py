def solution(s1, s2):
    # s1 = "abca"
    # s2 = "xyzbac"

    # Base the loop count on the length of the shorter string
    if len(s1) < len(s2):
        shorter_string = s1
        longer_string = s2
    else:
        shorter_string = s2
        longer_string = s1

    common_counter = 0
    for c1 in shorter_string:
        if c1 in longer_string:
            longer_string = list(longer_string)
            longer_string.remove(c1)
            longer_string = ''.join(longer_string)
            common_counter += 1

    return common_counter



if __name__ == "__main__":
    print(solution("abca", "xyzbac"))