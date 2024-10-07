#Q:1 Write a function that takes a list of numbers and returns the sum of those numbers.

def sum_of_numbers(numbers):
    return sum(numbers)
numbers = [1, 2, 3, 4, 5]
print(sum_of_numbers(numbers))


# Q:2 Write a program that doubles each element in a list of numbers. For example, if you start with this list:
# numbers = [1, 2, 3, 4]
# You should end with this list:

numbers = [2, 4, 6, 8]
def double_numbers(numbers):
    return [num * 2 for num in numbers]

numbers = [1, 2, 3, 4]
doubled_numbers = double_numbers(numbers)
print(doubled_numbers)


# Q:3 Implement an 'eraser' on a canvas.
# The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import tkinter as tk
import random

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400
CELL_SIZE = 20
ERASER_SIZE = 20
INITIAL_TIME = 60  

class EraserGame(tk.Canvas):
    def __init__(self, parent):
        super().__init__(parent, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.cells = []
        self.obstacles = []
        self.eraser_id = None
        self.score = 0
        self.time_left = INITIAL_TIME
        self.level = 1
        self.game_active = True

        self.create_grid()
        self.bind("<B1-Motion>", self.drag_eraser)

        self.score_label = tk.Label(parent, text=f"Score: {self.score}")
        self.score_label.pack()
        self.timer_label = tk.Label(parent, text=f"Time: {self.time_left}")
        self.timer_label.pack()

        self.update_timer()

    def create_grid(self):
        """Creates a grid of blue cells and random obstacles on the canvas."""
        for x in range(0, CANVAS_WIDTH, CELL_SIZE):
            row = []
            for y in range(0, CANVAS_HEIGHT, CELL_SIZE):
                if random.random() < 0.1:  
                    rect_id = self.create_rectangle(
                        x, y, x + CELL_SIZE, y + CELL_SIZE,
                        fill='red', outline='black'
                    )
                    self.obstacles.append(rect_id)
                else:
                    rect_id = self.create_rectangle(
                        x, y, x + CELL_SIZE, y + CELL_SIZE,
                        fill='blue', outline='black'
                    )
                row.append(rect_id)
            self.cells.append(row)

    def drag_eraser(self, event):
        """Handles the eraser dragging."""
        if not self.game_active:
            return  

        x, y = event.x, event.y
        if self.eraser_id is None:
            self.eraser_id = self.create_rectangle(
                x, y, x + ERASER_SIZE, y + ERASER_SIZE,
                outline='black', fill='white'
            )
        else:
            self.coords(self.eraser_id, x, y, x + ERASER_SIZE, y + ERASER_SIZE)

        self.erase_cells(x, y)

    def erase_cells(self, x, y):
        """Erases blue cells and handles obstacles."""
        for row in self.cells:
            for cell_id in row:
                cell_coords = self.coords(cell_id)
                if (cell_coords[2] > x and cell_coords[0] < x + ERASER_SIZE and
                    cell_coords[3] > y and cell_coords[1] < y + ERASER_SIZE):
                    if self.itemcget(cell_id, 'fill') == 'blue':
                        self.itemconfig(cell_id, fill='white')
                        self.score += 1
                        self.update_score()

        for obstacle_id in self.obstacles:
            obstacle_coords = self.coords(obstacle_id)
            if (obstacle_coords[2] > x and obstacle_coords[0] < x + ERASER_SIZE and
                obstacle_coords[3] > y and obstacle_coords[1] < y + ERASER_SIZE):
                self.end_game("Game Over! You hit an obstacle.")

    def update_score(self):
        """Updates the score display."""
        self.score_label.config(text=f"Score: {self.score}")

    def update_timer(self):
        """Decrements the timer and checks win/loss conditions."""
        if self.time_left > 0 and self.game_active:
            self.time_left -= 1
            self.timer_label.config(text=f"Time: {self.time_left}")
            self.after(1000, self.update_timer)
        else:
            if self.time_left <= 0:
                self.end_game("Time's Up! You Lose!")

    def end_game(self, message):
        """Ends the game and displays the game over message."""
        self.game_active = False
        self.create_text(CANVAS_WIDTH//2, CANVAS_HEIGHT//2, text=message, font=('Arial', 24), fill='red')
        self.unbind("<B1-Motion>")  

root = tk.Tk()
root.title("Advanced Eraser Game")

eraser_game = EraserGame(root)
eraser_game.pack()

root.mainloop()





#Q:4 In the information flow lesson, we discussed using a variable storing a number as an example of scope. We saw that changes we made to the number inside a function did not stay unless we returned it. This is true for what we call immutable data types which include things like numbers and strings.

# However, there are also mutable data types where changes stay even if we don't return anything. Some examples of mutable data types are lists and dictionaries. This means that you should be mindful when modifying lists and dictionaries within helper functions since their changes stay whether or not you return them.

# To see this in action, fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list. Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.

# Here is an example run of this program (user input in bold italics):

# Enter a message to copy: Hello world!

# List before: []

# List after: ['Hello world!', 'Hello world!', 'Hello world!']

# (Note. The concept of immutable/mutable data types is called mutability. Be careful because different programming languages have different rules regarding mutability!)



def add_three_copies(lst, data):
    lst.append(data)
    lst.append(data)
    lst.append(data)

if __name__ == "__main__":
    message = input("Enter a message to copy: ")
    
    my_list = []
    
    print("List before:", my_list)
    
    add_three_copies(my_list, message)
    
    print("List after:", my_list)



#Q:5 Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.


def get_first_element(lst):
    print("The first element is:", lst[0])

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the list: "))
    
    my_list = []
    
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)
    
    get_first_element(my_list)
    

#Q:6 Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(lst):
    print("The last element is:", lst[-1])

if __name__ == "__main__":
    n = int(input("Enter the number of elements in the list: "))
    
    my_list = []
    
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)
    
    get_last_element(my_list)


#Q:7 Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

def main():
    my_list = []
    
    while True:
        value = input("Enter a value: ")
        
        if value == "":
            break
        
        my_list.append(value)
    
    print("Here's the list:", my_list)

if __name__ == "__main__":
    main()



#Q:8 Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

MAX_LENGTH = 3  
def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_element = lst.pop()
        print("Removed:", removed_element)

def main():
    n = int(input("Enter the number of elements in the list: "))
    
    my_list = []
    
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)
    
    print("List before shortening:", my_list)
    
    shorten(my_list)
    
    print("List after shortening:", my_list)

if __name__ == "__main__":
    main()
