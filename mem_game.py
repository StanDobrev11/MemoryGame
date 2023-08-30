import os
import random
import math
import time

import player


# from string import ascii_letters
# import emoji
def clear():
    return os.system('cls')


class Memory:
    def __init__(self):
        self.count = self.set_board_dims()
        self.board = self.generate_board(self.count)
        self.nums = self.board_nums()

    def __str__(self):
        return f"Try to memorize as flws: \n" \
               f"{self.board}"

    @staticmethod
    def set_board_dims():
        is_valid_input = False
        count = None
        while not is_valid_input:
            user_input = input("Please set the length of the memory list: ")
            try:
                count = int(user_input)
                if count % 2 == 1:
                    count += 1
                if 4 <= count <= 10:
                    is_valid_input = True
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input. Try integer from 4 to 10")
        return count

    @staticmethod
    def generate_board(count):
        generated_board = []
        while len(generated_board) < count:
            list_emoji = ["\U0001F642", "\U0001F92A", "\U0001F61C", "\U0001F633", "\U0001F910", "\U0001F929",
                          "\U0001F970", "\U0001F923", "\U0001F60E", "\U0001F920"]
            letter = random.choice(list_emoji)
            # letter = random.choice(ascii_letters)
            generated_board.append(letter)
            generated_board = list(set(generated_board))

        working_list = generated_board.copy()
        while len(working_list) != 0:
            generated_board.append(random.choice(working_list))
            working_list.remove(generated_board[-1])
        return generated_board

    def print_board(self):
        side_a = int(math.sqrt(len(self.board)))
        side_b = len(self.board) // side_a
        for row in [self.board[i * side_a:(i + 1) * side_a] for i in range(side_b)]:
            print('| ' + ' | '.join(row) + ' |')

    def board_nums(self):
        num_list = [str(number) for number in range(10, len(self.board) + 11)]
        return num_list

    def print_board_nums(self, numbers_list):
        side_a = int(math.sqrt(len(self.board)))
        side_b = len(self.board) // side_a
        for row in [numbers_list[i * side_a:(i + 1) * side_a] for i in range(side_b)]:
            print('| ' + ' | '.join(row) + ' |')

    def print_board_with_guessed_elements(self, image_list, num_1, num_2):
        image_list[num_1] = self.board[num_1]
        image_list[num_2] = self.board[num_2]
        self.print_board_nums(image_list)

        return image_list

    def print_board_one_element(self, image_list, num_1):
        image_list[num_1] = self.board[num_1]
        self.print_board_nums(image_list)

    def board_length(self):
        return len(self.board)

    @staticmethod
    # def generate_players():
    #     players = mem.player_count()
    #     players_dict = {}
    #     for num in range(1, players + 1):
    #         user_input = input(f"Enter Player {num}\'s name: ")
    #         players_dict[num] = user_input
    #     return players_dict
    #
    # @staticmethod
    # def player_count():
    #     is_valid = False
    #     players = 1
    #     while not is_valid:
    #         user_input = input("How many players? Select 1 - 4: ")
    #         try:
    #             players = int(user_input)
    #             if players in range(1, 4 + 1):
    #                 is_valid = True
    #             else:
    #                 raise ValueError
    #         except ValueError:
    #             print("Invalid input")
    #
    #     return players

    def check_if_guessed(image_list, num_1, num_2, player):
        guessed = []
        if image_list[num_1] == image_list[num_2]:
            player.score += 1

            guessed.extend([num_1, num_2])
            mem.print_board_with_guessed_elements(mem.nums, num_1, num_2)
            print("Good guess!!")


        else:

            mem.print_board_with_guessed_elements(mem.nums, num_1, num_2)
            print("Wrong guess")
            time.sleep(1.5)
            clear()
            mem.nums[num_1] = str(num_1 + 10)
            mem.nums[num_2] = str(num_2 + 10)
            mem.print_board_nums(mem.nums)


class Player:
    def __init__(self, name):
        self.name = name

    def get_move(self, image_list):
        pass


class HumanPlayer(Player):
    def __init__(self, name):
        self.score = 0
        super().__init__(name)

    def get_move(self, image_list):
        is_first_valid = False
        is_second_valid = False
        first_guess = ""
        second_guess = ""

        while not is_first_valid:
            first_input = input("Please select first cell by its number: ")
            try:
                first_guess = int(first_input) - 10
                if first_guess not in range(mem.board_length()):
                    raise ValueError
                else:
                    clear()
                    mem.print_board_one_element(image_list, first_guess)
                    is_first_valid = True

            except ValueError:
                print(f"Invalid input. Try integer from 10 to {mem.board_length() + 9}")

        while not is_second_valid:
            second_input = input("Please select second cell by its number: ")
            try:
                second_guess = int(second_input) - 10
                if first_guess == second_guess:
                    raise ValueError
                elif first_guess not in range(mem.board_length() + 1):
                    raise ValueError
                else:
                    clear()
                    is_second_valid = True
            except ValueError:
                print(f"Invalid input. Try integer from 10 to {mem.board_length() + 9}")

        valid_guess = [first_guess, second_guess]
        return valid_guess
    # def get_move(self):
    #     is_guess_valid = False
    #     valid_guess = None
    #     while not is_guess_valid:
    #         user_input = input("Please select 2 cells by their number in format (NUM, NUM): ")
    #         try:
    #             valid_guess = list(map(int, user_input.split()))
    #             if valid_guess[0] == valid_guess[1]:
    #                 raise ValueError
    #             elif valid_guess[0] not in range(10, mem.board_length() + 10):
    #                 raise ValueError
    #             elif valid_guess[1] not in range(10, mem.board_length() + 10):
    #                 raise ValueError
    #             else:
    #                 is_guess_valid = True
    #         except ValueError:
    #             print(f"Invalid input. Try integer from 10 to {mem.board_length() + 9}")
    #
    #     return valid_guess


def play(m, pl_one, pl_two):
    print("Get ready to memorize the board.\nYou have 5 seconds!!\n3...\n2...\n1...")
    time.sleep(3)
    clear()
    m.print_board()
    time.sleep(5)
    clear()
    m.print_board_nums(m.nums)
    turn = pl_one
    while True:
        if turn == pl_one:
            guess = pl_one.get_move(mem.nums)
        else:
            guess = pl_two.get_move(mem.nums)
        guess = [int(el) for el in guess]
        guess = m.check_if_guessed(m.board, guess[0], guess[1], turn)


if __name__ == '__main__':
    player_1 = HumanPlayer("Ema")
    player_2 = HumanPlayer('Marti')
    mem = Memory()
    play(mem, player_1, player_2)
    print(mem.nums == mem.board)

# TODO game not ending when all are guessed





# mem = Memory()
# mem.print_board()
# # clear()
# mem.print_board_nums()
# # player_one = HumanPlayer("Ivi")
# # player_two = HumanPlayer("Sway")
# # print(player_one.name)
# # print(player_one.get_move())
# mem.generate_players()
