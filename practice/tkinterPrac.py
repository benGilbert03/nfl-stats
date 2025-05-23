import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def show_selection():
    selected = combo.get()
    label_result.config(text=f"You selected: {selected}")
    show_images()

def on_image_click(index):
    print(f"Image {index} clicked")

def load_image_from_url(url, size=(150, 150)):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).resize(size)
    return ImageTk.PhotoImage(img)

def show_images():
    # Show label
    label_result.pack()

    # Show image buttons
    image1_btn.pack(side="left", padx=20)
    image2_btn.pack(side="right", padx=20)

    # Show labels below images
    image1_label.pack(side="left", padx=20)
    image2_label.pack(side="right", padx=20)

# --- GUI Setup ---
root = tk.Tk()
root.title("Image Choice Example")

# Dropdown
options = [f"Option {i}" for i in range(1, 12)]
combo = ttk.Combobox(root, values=options, state="readonly")
combo.current(0)
combo.pack(pady=10)

# Submit button
tk.Button(root, text="Submit", command=show_selection).pack(pady=10)

# Label (initially hidden)
label_result = tk.Label(root, text="", font=("Arial", 14))

# Load images (resized for display)
url1 = "https://static.www.nfl.com/image/upload/f_auto,q_auto/league/lngo1onvkcqjnq7ozkuu"
url2 = "https://static.www.nfl.com/image/upload/f_auto,q_auto/league/hqb9xnzm9brx79zl6wve"
img1_tk = load_image_from_url(url1)
img2_tk = load_image_from_url(url2)

# Images as buttons
image1_btn = tk.Button(root, image=img1_tk, command=lambda: on_image_click(1))
image2_btn = tk.Button(root, image=img2_tk, command=lambda: on_image_click(2))

# Labels below images
image1_label = tk.Label(root, text="This is Image 1")
image2_label = tk.Label(root, text="This is Image 2")

root.mainloop()
