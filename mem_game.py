import os
import random
import math
import time


# from string import ascii_letters
# import emoji
def clear():
    return os.system('cls')


class Memory:
    def __init__(self):
        self.count = 10  # self.user_input()
        self.board = self.generate_board(self.count)

    def __str__(self):
        return f"Try to memorize as flws: \n" \
               f"{self.board}"

    @staticmethod
    def user_input():
        is_valid_input = False
        while not is_valid_input:
            user_input = input("Please set the length of the memory list: ")
            try:
                count = int(user_input)
                if count % 2 == 1:
                    count += 1
                if 4 <= count <= 10:
                    return count
                raise ValueError
            except ValueError:
                print("Invalid input. Try integer from 4 to 10")

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

    def print_board_nums(self):
        side_a = int(math.sqrt(len(self.board)))
        side_b = len(self.board) // side_a
        num_list = [str(number) for number in range(10, len(self.board) + 11)]
        for row in [num_list[i * side_a:(i + 1) * side_a] for i in range(side_b)]:
            print('| ' + ' | '.join(row) + ' |')


mem = Memory()
mem.print_board()
# clear()
mem.print_board_nums()
