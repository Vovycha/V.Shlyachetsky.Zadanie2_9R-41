
import random

board = [' '] * 9
player = 'X'
computer = 'O'

def print_board():
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print("\n")

def check_winner():
    win_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    for line in win_lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != ' ':
            return board[line[0]]
    
    if ' ' not in board:
        return 'Ничья'
    
    return None

def player_move():
    while True:
        try:
            move = int(input("Ваш ход (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                board[move] = player
                return
            else:
                print("Некорректный ход. Попробуйте еще раз.")
        except:
            print("Введите число от 1 до 9.")

def computer_move():
    for i in range(9):
        if board[i] == ' ':
            board[i] = computer
            if check_winner() == computer:
                return
            board[i] = ' '
    
    for i in range(9):
        if board[i] == ' ':
            board[i] = player
            if check_winner() == player:
                board[i] = computer
                return
            board[i] = ' '
    
    if board[4] == ' ':
        board[4] = computer
        return
    
    empty_cells = [i for i in range(9) if board[i] == ' ']
    if empty_cells:
        board[random.choice(empty_cells)] = computer

def play_game():
    print("=" * 30)
    print(" КРЕСТИКИ-НОЛИКИ ПРОТИВ КОМПЬЮТЕРА")
    print("=" * 30)
    print("\nИгровое поле нумеруется так:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\nВы играете за X, компьютер за O\n")
    
    global board
    board = [' '] * 9
    current_player = player
    
    while True:
        print_board()
        
        if current_player == player:
            player_move()
        else:
            print("Ход компьютера...")
            computer_move()
        
        result = check_winner()
        if result:
            print_board()
            if result == player:
                print("ПОЗДРАВЛЯЮ! Вы победили!")
            elif result == computer:
                print("Компьютер победил!")
            else:
                print("Ничья!")
            break
        
        current_player = computer if current_player == player else player

def main():
    while True:
        play_game()
        play_again = input("\nСыграть еще раз? (да/нет): ").lower()
        if play_again not in ['да', 'д', 'yes', 'y']:
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    main()
