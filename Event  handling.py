import tkinter as tk

window = tk.Tk()
# pad x for horizontal of label and y for vertical
label = tk.Label(window, text="Hello, Tkinter!", fg="blue", bg="yellow", padx=10, pady=5)
label.pack()

button = tk.Button(window, text="Click Me", width=15, command=lambda: print("Button clicked!"))
button.pack()


window.mainloop()
# lambda is a function with no name for one time and one line
