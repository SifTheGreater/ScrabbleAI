import random
import tkinter as tk

class ScrabbleBoard:
    def __init__(self):
        self.board = self.create_board()
        self.letter_bag = self.create_letter_bag()
        self.score_board = {}

    def create_board(self):
        # Initialize an empty 15x15 board
        return [[' ' for _ in range(15)] for _ in range(15)]

    def create_letter_bag(self):
        # Create a dictionary containing the letter distribution in the game
        letter_distribution = {
            'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9,
            'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6,
            'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, '?': 2
        }
        letter_bag = []
        for letter, count in letter_distribution.items():
            letter_bag.extend([letter] * count)
        return letter_bag


class ScrabbleGame:
    def __init__(self):
        self.board = ScrabbleBoard()
        self.players = []
        self.current_turn = 0

    def add_player(self, player):
        self.players.append(player)
        self.board.score_board[player] = 0
        self.draw_tiles(player, 7)

    def draw_tiles(self, player, count):
        for _ in range(count):
            if not self.board.letter_bag:
                break
            tile = random.choice(self.board.letter_bag)
            self.board.letter_bag.remove(tile)
            player.tiles.append(tile)

    def play_turn(self, player, word, row, col, direction):
        # Place the tiles on the board and update the player's score
        # Remove used tiles from the player's rack and draw new tiles
        pass

class ScrabbleGUI(tk.Tk):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.title("Scrabble Game")
        self.geometry("1500x1200")
        self.attributes('-fullscreen', True)
        self.create_quit_buttons()
        self.create_board()


    def create_board(self):
        self.board_frame = tk.Frame(self)
        self.board_frame.pack(padx=10, pady=10)

        self.board_buttons = []
        for i in range(15):
            row = []
            for j in range(15):
                button = tk.Button(self.board_frame, text="{i}, {j}".format(i=i, j=j), width=4, height=2)
                button.grid(row=i, column=j)
                row.append(button)
            self.board_buttons.append(row)

        self.current_player_label = tk.Label(self, text="Current player: ")
        self.current_player_label.pack(pady=10)

    def create_quit_buttons(self):
        #due to padding in frame creation we can only place things as far down as 20
        self.Quit_Frame = tk.Frame(self)
        self.Quit_Frame.pack(side=tk.TOP, anchor=tk.E, padx=10, pady=10, fill=tk.X)

        quit_button = tk.Button(self.Quit_Frame, text="Quit", command=self.quit_game, width=15, height=1)
        quit_button.pack(side=tk.RIGHT, padx=5, pady=5)

        quit_button2 = tk.Button(self.Quit_Frame, text="Left Quit", command=self.quit_game, width=15, height=1)
        quit_button2.pack(side=tk.LEFT, padx=5, pady=5)

        quit_button3 = tk.Button(self.Quit_Frame, text="Extra Quit", command=self.quit_game, width=15, height=1, fg="white", bg="red", activebackground="orange")
        quit_button3.place(x=1500, y=5)

    def quit_game(self):
        self.destroy()

        # Add more widgets for player's rack and action buttons

        # according to kat we need the following buttons
        # play word
        # swap letters
        # pass turn
        # take blank - doesnt take your turn

def main():
    game = ScrabbleGame()  # Initialize the game logic
    gui = ScrabbleGUI(game)
    gui.mainloop()


if __name__ == "__main__":
    main()