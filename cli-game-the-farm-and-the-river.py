"""
witten by chatGPT with promt:
User
in python, I want to write the farmer, boat, fox, goose and corn riddle as a text based game. with the commands to use being "take x, leave x, go north, go south"
"""
# running this program in this state is a great example of why you cant relay on chatGPT to just write your code and trust it to work. 

class Game:
    def __init__(self):
        self.left_bank = {'farmer', 'fox', 'goose', 'corn'}
        self.right_bank = set()
        self.boat = set()
        self.game_over = False

    def display_state(self):
        print(f'Left Bank: {self.left_bank}')
        print(f'Right Bank: {self.right_bank}')
        print(f'Boat: {self.boat}')

    def move_boat(self):
        if 'farmer' in self.boat:
            if not self.boat.issubset(self.left_bank):
                self.left_bank -= self.boat
                self.right_bank.update(self.boat)
                self.boat.clear()
            else:
                self.right_bank -= self.boat
                self.left_bank.update(self.boat)
                self.boat.clear()
        else:
            print("The farmer must be on the boat to move.")

    def check_game_over(self):
        if len(self.left_bank) == 0:
            print("Congratulations! You have successfully transported the fox, goose, and corn to the other side.")
            self.game_over = True
        elif 'farmer' in self.left_bank and ('fox' in self.left_bank and 'goose' in self.left_bank):
            print("Oops! The fox ate the goose. Game Over!")
            self.game_over = True
        elif 'farmer' in self.left_bank and ('goose' in self.left_bank and 'corn' in self.left_bank):
            print("Oops! The goose ate the corn. Game Over!")
            self.game_over = True

    def play(self):
        print("Welcome to the Farmer, Fox, Goose, and Corn Riddle!")
        print("Commands: take x, leave x, go north, go south, exit")

        while not self.game_over:
            self.display_state()
            command = input("Enter your command: ").split()
            action = command[0].lower()

            if action == "take" or action == "leave":
                item = command[1].lower()
                if item in self.left_bank or item in self.right_bank:
                    if action == "take" and item != 'farmer' and item not in self.boat:
                        self.boat.add(item)
                    elif action == "leave" and item in self.boat:
                        self.boat.remove(item)
                    else:
                        print("You can't do that.")
                else:
                    print(f"There is no {item} here.")
            elif action == "go":
                direction = command[1].lower()
                if direction == "north" or direction == "south":
                    self.move_boat()
                    self.check_game_over()
                else:
                    print("Invalid direction. Use 'go north' or 'go south'.")
            elif action == "exit":
                print("Goodbye! Thanks for playing.")
                break
            else:
                print("Invalid command. Please try again.")


if __name__ == "__main__":
    game = Game()
    game.play()
