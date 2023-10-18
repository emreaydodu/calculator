import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            # Evaluate the expression and calculate the result
            result = str(eval(screen.get()))
            # Add the expression and result to the history
            expression = f"{screen.get()} = {result}"
            screen.set(result)
            history.insert(tk.END, expression)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        # Clear the screen
        screen.set("")
    elif text == "MC":
        # Clear memory
        memory.set("")
    elif text == "M+":
        # Add to memory
        current_memory = memory.get()
        if current_memory:
            current_memory += "+" + screen.get()
        else:
            current_memory = screen.get()
        memory.set(current_memory)
    elif text == "M-":
        # Subtract from memory
        current_memory = memory.get()
        if current_memory:
            current_memory += "-" + screen.get()
        else:
            current_memory = screen.get()
        memory.set(current_memory)
    elif text == "MR":
        # Read memory and display it on the screen
        screen.set(memory.get())
    else:
        # Update the screen
        current_text = screen.get()
        current_text += text
        screen.set(current_text)

# Create a Tkinter window
root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")
root.configure(bg="#F5F5F5")

# StringVar for the screen
screen = tk.StringVar()

# Screen (Entry) for the calculator
entry = tk.Entry(root, textvar=screen, font=("Arial", 30), bd=10, insertwidth=4, width=14, justify="right", bg="#D3D3D3")
entry.grid(row=0, column=0, columnspan=4)

# Frame for the calculator buttons
button_frame = tk.Frame(root, bg="#F5F5F5")
button_frame.grid(row=1, column=0)

# Calculator buttons
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create and style the buttons
i = 0
for btn in button_texts:
    button = tk.Button(button_frame, text=btn, font=("Arial", 20), padx=20, pady=20, bd=8, width=3, height=1)
    button.grid(row=i // 4, column=i % 4)
    button.configure(bg="#99A3A4", activebackground="#DDA0DD", fg="black", activeforeground="white")
    button.bind("<Button-1>", on_click)
    i += 1

# Frame for the history section
history_frame = tk.Frame(root, bg="#F5F5F5")
history_frame.grid(row=2, column=0)

# Label for the history section
history_label = tk.Label(history_frame, text="History", font=("Arial", 16), bg="#F5F5F5")
history_label.pack()

# Listbox for displaying the history
history = tk.Listbox(history_frame, font=("Arial", 12), bg="#D3D3D3", selectbackground="white")
history.pack()

# StringVar for the memory section
memory = tk.StringVar()

# Label for the memory section
memory_label = tk.Label(root, textvar=memory, font=("Arial", 14), bg="#F5F5F5")
memory_label.grid(row=3, column=0, columnspan=4, sticky="W")

# Start the Tkinter window
root.mainloop()
