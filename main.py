from random import randint


class TankGame:
    def __init__(self):
        self.tank = '^'
        self.target = 'o'
        self.row, self.column = self.generate_random_position()
        self.target_row, self.target_column = self.generate_random_position()
        self.moves = {
            'up': 0,
            'down': 0,
            'left': 0,
            'right': 0,
        }
        self.moves_left = 5
        self.direction = None
        self.play_game = True

    def generate_game_board(self):
        game_info = (
            f'Tank moved: up - {self.moves["up"]} times, down - {self.moves["down"]} times,'
            f'left - {self.moves["left"]} times, right - {self.moves["right"]} times \n'
            f'Tank coordinates: {self.row + 1}, {self.column + 1} Tank direction: {tank.direction} \n'
            f'Moves left: {self.moves_left}'
        )
        print(game_info)
        print('  1 2 3 4 5 6 7 8 9 ')
        for row in range(9):
            board = str(row + 1) + ' '
            for col in range(9):
                if row == self.target_row and col == self.target_column:
                    board += self.target + '|'  # target
                elif row == self.row and col == self.column:
                    board += self.tank + '|'
                else:
                    board += ' |'
            print(board)

    def generate_random_position(self):
        return randint(0, 8), randint(0, 8)

    def choose_action(self):
        while self.play_game and self.moves_left > 0:
            self.generate_game_board()
            action = input('CHOOSE YOUR MOVE: m - move tank, s - shoot, q - quit: ')
            if action.lower() == 'm':
                direction = input('ENTER DIRECTION: w - up, s - down, a - left, d - right: ')
                self.move(direction)
            elif action.lower() == 's':
                self.shoot()
            elif action.lower() == 'q':
                print('QUITTING THE GAME.... THANK YOU FOR PLAYING!')
                self.play_game = False
            else:
                print('Sorry, that direction is not valid..')

        if self.moves_left == 0:
            print('YOU DIDN`T HIT THE TARGET ON TIME! GAME OVER!')
            self.game_over()

    def move(self, direction):
        if direction.lower() in ['w', 's', 'a', 'd']:
            if direction.lower() == 'w':
                if self.row > 0:
                    self.row -= 1
                    self.tank = '^'
                    self.moves['up'] += 1
                    self.direction = 'w'
            elif direction.lower() == 's':
                if self.row < 8:
                    self.row += 1
                    self.tank = 'v'
                    self.moves['down'] += 1
                    self.direction = 's'
            elif direction.lower() == 'a':
                if self.column > 0:
                    self.column -= 1
                    self.tank = '<'
                    self.moves['left'] += 1
                    self.direction = 'a'
            elif direction.lower() == 'd':
                if self.column < 8:
                    self.column += 1
                    self.tank = '>'
                    self.moves['right'] += 1
                    self.direction = 'd'
            self.moves_left -= 1

            if self.row == self.target_row and self.column == self.target_column:
                print('YOU HIT THE BOMB! TANK EXPLODED! GAME OVER!')
                self.game_over()
        else:
            print('CANNOT MOVE IN THAT DIRECTION. TRY AGAIN.')

    def shoot(self):
        if self.direction:
            if (self.direction == 'a' and self.target_column < self.column) or \
                    (self.direction == 'd' and self.target_column > self.column) or \
                    (self.direction == 'w' and self.target_row < self.row) or \
                    (self.direction == 's' and self.target_row > self.row):
                print('WELL DONE! TANK WIN!')
                self.game_over()
            elif self.row == self.target_row and self.column == self.target_column:
                print('YOU HIT THE BOMB! TANK EXPLODED! GAME OVER')
                self.game_over()
            else:
                print('TANK MISSED THE TARGET!')

    def game_over(self):
        while True:
            play_again = input('Would you like to play again? y - yes, n - no:')
            if play_again.lower() == 'y':
                self.row, self.column = self.generate_random_position()
                self.target_row, self.target_column = self.generate_random_position()
                self.direction = None
                self.moves = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
                self.moves_left = 5
                print('NEW GAME:')
                self.choose_action()
                break
            elif play_again.lower() == 'n':
                print('THANK YOU FOR PLAYING!')
                self.play_game = False
                break
            else:
                print('Invalid input. Please enter "y" or "n"')




tank = TankGame()
tank.choose_action()

