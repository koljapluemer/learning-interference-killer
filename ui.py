import os
import shutil
import tkinter as tk
# pillow
from PIL import Image, ImageTk
import random

class Purger:
    def __init__(self, root):
        self.root = root
        # folder path is current path
        self.folder_path = os.path.dirname(os.path.realpath(__file__))
        # get all image files in the folder
        folder_1 = os.path.join(self.folder_path, 'problems/00/Differenz')
        folder_2 = os.path.join(self.folder_path, 'problems/00/Division')

        self.image_list_1 = [f for f in os.listdir(folder_1) if f.endswith('.png')]
        self.image_list_2 = [f for f in os.listdir(folder_2) if f.endswith('.png')]

        self.root.configure(bg="#222222")  # Set background color to dark gray

        self.html_label = tk.Label(root)
        self.html_label.pack(fill="both", expand=True)
        self.img_label = tk.Label(root)
        self.img_label.place(relx=0.5, rely=0.5, anchor="center")

        self.load_file()

        self.btn_1 = tk.Button(root, text="← Differenz", command=lambda: self.answer(1), bg="#333333", fg="#ffffff", font=("Arial", 14))
        self.btn_1.pack(padx=10, pady=10, side=tk.LEFT, fill=tk.X)

        self.btn_2 = tk.Button(root, text="Division →", command=lambda: self.answer(2), bg="#333333", fg="#ffffff", font=("Arial", 14))
        self.btn_2.pack(padx=10, pady=10, side=tk.RIGHT, fill=tk.X)



        # Bind arrow keys to button actions
        root.bind("<Left>", lambda event: self.answer(1))
        root.bind("<Right>", lambda event: self.answer(2))

    def answer(self, answer):
        print(f"Answer: {answer}")
        self.load_file()

    def load_file(self):
        decide_from_which_folder = random.randint(0, 1) + 1
        if decide_from_which_folder == 1:
            relevant_img_list = self.image_list_1
            self.currently_picked_folder = 'Differenz'
        else:
            relevant_img_list = self.image_list_2
            self.currently_picked_folder = 'Division'
        random_file = random.choice(relevant_img_list)
        file_path = os.path.join(self.folder_path, 'problems', '00', self.currently_picked_folder, random_file)
        with open(os.path.join(self.folder_path, 'problems', '00', self.currently_picked_folder, random_file), 'rb') as file:
            img = Image.open(file)
            img_tk = ImageTk.PhotoImage(img)
            # Set image to label
            self.img_label.configure(image=img_tk)
            self.img_label.image = img_tk


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sachen Unterscheiden")
    root.geometry("800x600")  # Set initial window size
    root.configure(bg="#222222")  # Set background color to dark gray
    viewer = Purger(root)
    root.mainloop()
