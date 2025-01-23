import tkinter as tk
from tkinter import Label
from PIL import ImageTk, Image
from random import randint
from tkinter import ttk


root = tk.Tk()
root.title('Rock Paper Scissors')
root.geometry("800x600")  # Adjusted window size for better visibility
root.config(bg="white")  # Background color set to white

# Rock Paper Scissors Images - Load images using PIL and resize them
rock_image = ImageTk.PhotoImage(Image.open('/Users/ayan/PycharmProjects/pythonProject1/.venv/Assets/rock.png').resize((500, 500)))
paper_image = ImageTk.PhotoImage(Image.open('/Users/ayan/PycharmProjects/pythonProject1/.venv/Assets/paper1.png').resize((500, 500)))
scissors_image = ImageTk.PhotoImage(Image.open('/Users/ayan/PycharmProjects/pythonProject1/.venv/Assets/scissors.png').resize((500, 500)))

# List of images
image_list = [rock_image, paper_image, scissors_image]

# Function to spin and display a random image
def spin():
    #Pick random number
    pick_number = randint(0, 2)
    #Show image
    image_label.config(image=image_list[pick_number])

    # 0 = Rock
    # 1 = Paper
    # 2 = Scissors

    #Convert Dropdown choice to a number
    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissors":   # You can use the 'else'
        user_choice_value = 2

    #Determine if we won or lost
    if user_choice_value == 0: # Rock
        if pick_number == 0:
            win_lose_label.config(text="It's a Tie! Spin Again!")
        elif pick_number == 1:   # Paper
            win_lose_label.config(text="Paper covers Rock! You Lose!")
        elif pick_number == 2:  # Scissors
            win_lose_label.config(text="Rock smashes Scissors! You Win!")
# If user picks paper
    if user_choice_value == 1:  # Paper
        if pick_number == 1:
            win_lose_label.config(text="It's a Tie! Spin Again!")
        elif pick_number == 0:  # Rock
            win_lose_label.config(text="Paper covers Rock! You Win!")
        elif pick_number == 2:  # Scissors
            win_lose_label.config(text="Scissors cuts Paper! You Lose!")
#If User picks scissors
    if user_choice_value == 2:  # Scissors
        if pick_number == 2:
            win_lose_label.config(text="It's a Tie! Spin Again!")
        elif pick_number == 0:  # Rock
            win_lose_label.config(text="Rock Smashes Scissors! You Lose!")
        elif pick_number == 1:  # Paper
            win_lose_label.config(text="Scissors cuts Paper! You Win!")


#Make our choice
user_choice = ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=20)

# Create the "Spin" button
spin_button = tk.Button(root, text="Spin!", command=spin)
spin_button.pack(pady=10)

#Label for showing if you won or not
win_lose_label = tk.Label(root, text="", font=("Helvetica", 18))
win_lose_label.pack(pady=50)

# Display a random image initially
random_number = randint(0, 2)
image_label = Label(root, image=image_list[random_number])
image_label.image = image_list[random_number]  # Keep a reference to the image
image_label.pack(pady=20)

root.mainloop()
