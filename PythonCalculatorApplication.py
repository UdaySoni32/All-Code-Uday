import tkinter as tk
root = tk.Tk()
root.title("Calculator")  # Set the window title
root.geometry("312x324")  # Set the initial window size
root.resizable(0, 0)  # Prevent resizing the window
expression = ""  # Variable to store the mathematical expression
input_text = tk.StringVar()
input_field = tk.Entry(root, textvariable=input_text, font=('Arial', 24, 'bold'), bd=10, insertwidth=4, width=14, justify='right') 
input_field.grid(row=0, column=0, columnspan=4) # Place the input field in the grid
def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def bt_clear():
    global expression
    expression = ""
    input_text.set("")

def bt_equal():
    global expression
    try:
        result = str(eval(expression))  # Evaluate the expression
        input_text.set(result)
        expression = ""  # Clear the expression after calculation
    except:
        input_text.set("Error") # Display "Error" if evaluation fails
        expression = ""
# Create frames for buttons to manage their layout
btn_frame = tk.Frame(root, bg="lightgray")
btn_frame.grid(row=1, column=0, columnspan=4, sticky="nsew")

# Customize button styles
button_style = {'font': ('Arial', 16), 'width': 4, 'height': 2, 'bd': 2, 'relief': 'raised'}

# Create buttons for numbers and operators in a grid
buttons = [
    ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
    ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
    ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
    ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(btn_frame, text=text, command=bt_equal, **button_style).grid(row=row, column=col)
    else:
        tk.Button(btn_frame, text=text, command=lambda t=text: btn_click(t), **button_style).grid(row=row, column=col)

# Clear button
tk.Button(root, text="C", command=bt_clear, font=('Arial', 16), width=28, height=2, bd=2, relief='raised').grid(row=4, column=0, columnspan=4)
root.mainloop()
