N = 8  # 원하는 체스판 크기

board = [-1] * N  # board[i] = i번째 행에 퀸이 놓인 열 번호

def is_safe(row, col):
    for prev_row in range(row):
        # 같은 열 or 같은 대각선
        if board[prev_row] == col or abs(board[prev_row] - col) == abs(prev_row - row):
            return False
    return True

def place_queen(row):
    if row == N:
        print_board()
        return

    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            place_queen(row + 1)
            board[row] = -1  # 백트래킹

def print_board():
    for i in range(N):
        line = ['.'] * N
        line[board[i]] = 'Q'
        print(' '.join(line))
    print()

# 실행
place_queen(0)
