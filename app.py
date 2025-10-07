import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

image_list = []


def select_images():
    global image_list
    file_paths = filedialog.askopenfilenames(
        title="Select images", filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )
    if file_paths:
        for path in file_paths:
            if path not in image_list:
                image_list.append(path)
                listbox.insert(tk.END, os.path.basename(path))


def create_gif():
    if not image_list:
        messagebox.showerror("Error", "No images selected!")
        return
    try:
        duration = int(duration_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid duration.")
        return
    try:
        images = [Image.open(img).convert("RGBA") for img in image_list]
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load image:\n{e}")
        return
    save_path = filedialog.asksaveasfilename(
        defaultextension=".gif", filetypes=[("GIF files", "*.gif")], title="Save GIF as"
    )
    if save_path:
        try:
            images[0].save(
                save_path,
                save_all=True,
                append_images=images[1:],
                duration=duration,
                loop=0,
            )
            messagebox.showinfo("Success", f"GIF saved to:\n{save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save GIF:\n{e}")


def clear_list():
    global image_list
    image_list.clear()
    listbox.delete(0, tk.END)


root = tk.Tk()
root.title("img2gif")
root.geometry("440x510")
root.configure(bg="#f4f4f4")

tk.Label(
    root, text="img2gif", font=("Helvetica", 20, "bold"), bg="#f4f4f4", fg="#333"
).pack(pady=15)

listbox = tk.Listbox(
    root,
    width=50,
    height=10,
    font=("Courier", 10),
    bg="white",
    borderwidth=1,
    relief="solid",
)
listbox.pack(pady=10)

tk.Label(root, text="Duration (ms):", bg="#f4f4f4", font=("Helvetica", 11)).pack(
    pady=(15, 5)
)

duration_entry = tk.Entry(root, font=("Helvetica", 11), justify="center", width=10)
duration_entry.insert(0, "300")
duration_entry.pack(pady=5)

button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=30)

tk.Button(
    button_frame,
    text="Select",
    command=select_images,
    font=("Helvetica", 10),
    bg="#007acc",
    fg="white",
    activebackground="#005b9a",
    relief="flat",
    padx=10,
    pady=5,
    width=14,
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Clear List",
    command=clear_list,
    font=("Helvetica", 10),
    bg="#e74c3c",
    fg="white",
    activebackground="#c0392b",
    relief="flat",
    padx=10,
    pady=5,
    width=14,
).pack(side="left", padx=5)

tk.Button(
    button_frame,
    text="Create GIF",
    command=create_gif,
    font=("Helvetica", 10, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    relief="flat",
    padx=10,
    pady=5,
    width=14,
).pack(side="left", padx=5)

root.mainloop()
