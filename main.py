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

class Player:
    def __init__(self, name):
        self.name = name
        self.tiles = []
        self.score = 0

    def add_score(self, points):
        self.score += points

    def __str__(self):
        return f"{self.name} - {self.score} points"


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
        self.create_color_index()
        self.create_board()

    def get_tile_color(self, row, col):
        triple_word = [(0, 0), (0, 7), (0, 14), (7, 0), (14, 0), (14, 7), (14, 14), (7, 14)]
        double_word = [(1, 1), (2, 2), (3, 3), (4, 4), (1, 13), (2, 12), (3, 11), (4, 10), (10, 10), (11, 11), (12, 12),
                       (13, 13), (13, 1), (12, 2), (11, 3), (10, 4)]
        triple_letter = [(1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5),
                         (13, 9)]
        double_letter = [(0, 3), (0, 11), (3, 0), (3, 14), (3, 7), (2, 6), (2, 8), (6, 2), (6, 6), (6, 8), (6, 12),
                         (8, 2), (8, 6), (8, 8), (8, 12),
                         (7, 3), (7, 11), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11)]
        middle = [(7, 7)]

        if (row, col) in triple_word:
            return "#e10000"
        elif (row, col) in double_word:
            return "#ff89c2"
        elif (row, col) in triple_letter:
            return "#002fe7"
        elif (row, col) in double_letter:
            return "#99f1ff"
        elif (row, col) in middle:
            return "#82ff91"
        else:
            return "white"

    def create_color_index(self):
        self.Color_Index_Frame = tk.Frame(self)
        self.Color_Index_Frame.place(x=500, y=255)

        index_items = [
            ("#e10000", "   = Triple Word"),
            ("#ff89c2", "      = Double Word"),
            ("#002fe7", "   = Triple Letter"),
            ("#99f1ff", "     = Double Letter"),
            ("#82ff91", "= Center Tile")
        ]

        for i, (color, description) in enumerate(index_items):
            color_label = tk.Label(self.Color_Index_Frame, background=color, width=4, height=2)
            color_label.grid(row=i, column=0, padx=0, pady=5)

            # labels arnt compeltely aligned for some reason, will have to fix later.
            text_label = tk.Label(self.Color_Index_Frame, text=f" {description}", justify='left')
            text_label.grid(row=i, column=1, padx=0, pady=5)

    def create_board(self):
        self.board_frame = tk.Frame(self)
        self.board_frame.pack(padx=10, pady=10)

        self.board_buttons = []
        for i in range(15):
            row = []
            for j in range(15):
                tile_color = self.get_tile_color(i, j)
                button = tk.Button(self.board_frame, text=" ", width=4, height=2, bg=tile_color, activebackground="#b6b6b6")
                button.grid(row=i, column=j)
                row.append(button)
            self.board_buttons.append(row)

    def create_quit_buttons(self):
        # due to padding in frame creation we can only place things as far down as 20
        self.Quit_Frame = tk.Frame(self)
        self.Quit_Frame.pack(side=tk.TOP, anchor=tk.E, padx=10, pady=10, fill=tk.X)

        quit_button = tk.Button(self.Quit_Frame, text="Quit", command=self.quit_game, width=15, height=1,
                                fg="white", bg="red", activebackground="orange")
        quit_button.pack(side=tk.RIGHT, padx=5, pady=5)

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
    kathryn = Player("Kathryn")
    game.add_player(kathryn)

    nathan = Player("Nathan")
    game.add_player(nathan)

    gui = ScrabbleGUI(game)
    gui.mainloop()


if __name__ == "__main__":
    main()
