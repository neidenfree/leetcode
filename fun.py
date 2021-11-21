def spiral_matrix(n: int):
    def print_mat(mat) -> None:
        for i in range(len(mat)):
            for j in range(len(mat)):
                print(mat[i][j], end=' ')
            print()

    if n < 1:
        return None
    if n == 1:
        return [1]
    if n % 2 == 0:
        return None

    mat = [[0 for x in range(n)] for x in range(n)]
    i = n // 2
    j = n // 2
    direction = ['right', 'down', 'left', 'up']
    d = 0

    move_max = 1
    move_count = 0
    move_two = 0

    for s in range(1, n ** 2 + 1):
        print(f'{s} iteration, [{i},{j}], direction={direction[d]}')
        mat[i][j] = s
        print_mat(mat)
        move_count += 1
        if direction[d] == 'right':
            j += 1
        if direction[d] == 'down':
            i += 1
        if direction[d] == 'left':
            j -= 1
        if direction[d] == 'up':
            i -= 1

        if move_count == move_max:
            d += 1
            if d > 3:
                d = 0
            move_count = 0
            move_two += 1

        if move_two == 2:
            move_max += 1
            move_two = 0

    print_mat(mat)
    return mat


if __name__ == "__main__":
    spiral_matrix(3)
