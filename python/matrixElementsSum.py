def solution(matrix):
    total_cost = 0
    unwanted_rooms_index = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                unwanted_rooms_index.append(j)
            elif j not in unwanted_rooms_index:
                total_cost += matrix[i][j]

    return total_cost


if __name__ == "__main__":
    #matrix = [[0, 1, 1, 2], 
    #          [0, 5, 0, 0], 
    #          [2, 0, 3, 3]]

    matrix = [[1, 1, 1, 0], 
             [0, 5, 0, 1], 
             [2, 1, 3, 10]]

    print(solution(matrix))