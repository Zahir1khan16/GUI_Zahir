import tkinter as tk

def change_color():
    background_color=button.cget("bg")
    if background_color=="green":
        button.config(bg="red")
    else:
        button.config(bg="green")

window=tk.Tk()
button = tk.Button(window, text="Click Me", width=15, command=change_color)
button.pack()
## command is used for functions

window.mainloop()
## button click changed cget vs config
## and also push on git