# Project 1 - Simple Calculator
# Version 3 - Scientific GUI
# 9/4/2026

import tkinter as tk
import math



# MAIN WINDOW


root = tk.Tk()

root.title("Scientific Calculator")
root.geometry("500x750")
root.resizable(False, False)



# VARIABLES


current_expression = ""
history = []

# Calculator starts in degrees
angle_mode = "DEG"



# DISPLAY


display = tk.Entry(
    root,
    font=("Arial", 26),
    justify="right",
    bd=10,
    relief="sunken"
)

display.pack(
    padx=15,
    pady=15,
    fill="x",
    ipady=10
)



# BASIC FUNCTIONS


def update_display():

    display.delete(0, tk.END)

    display.insert(
        0,
        current_expression
    )


def add_to_display(value):

    global current_expression

    current_expression += str(value)

    update_display()


def clear_display():

    global current_expression

    current_expression = ""

    update_display()


def delete_last():

    global current_expression

    current_expression = current_expression[:-1]

    update_display()


def toggle_sign():

    global current_expression

    try:

        number = float(current_expression)

        number = -number

        current_expression = str(number)

        update_display()

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Invalid number")

        current_expression = ""


# BASIC CALCULATION


def calculate():

    global current_expression

    try:

        expression = current_expression

        # Convert calculator symbols into Python operators
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        result = eval(expression)

        result = round(result, 10)

        calculation = f"{current_expression} = {result}"

        history.append(calculation)

        current_expression = str(result)

        update_display()

    except ZeroDivisionError:

        display.delete(0, tk.END)
        display.insert(0, "Can't divide by zero")

        current_expression = ""

    except (SyntaxError, ValueError):

        display.delete(0, tk.END)
        display.insert(0, "Invalid expression")

        current_expression = ""


# =========================================================
# SCIENTIFIC HELPER
# =========================================================

def get_current_number():

    try:

        return float(current_expression)

    except ValueError:

        raise ValueError


def show_result(calculation, result):

    global current_expression

    result = round(result, 10)

    history.append(
        f"{calculation} = {result}"
    )

    current_expression = str(result)

    update_display()


# =========================================================
# SQUARE ROOT
# =========================================================

def square_root():

    try:

        number = get_current_number()

        if number < 0:
            raise ValueError

        result = math.sqrt(number)

        show_result(
            f"√{number}",
            result
        )

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Invalid number")

        clear_after_error()


# =========================================================
# SQUARE
# =========================================================

def square():

    try:

        number = get_current_number()

        result = math.pow(number, 2)

        show_result(
            f"{number}²",
            result
        )

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Invalid number")

        clear_after_error()


# =========================================================
# POWER
# =========================================================

def power():

    global current_expression

    try:

        number = get_current_number()

        current_expression = str(number) + "**"

        update_display()

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Invalid number")

        clear_after_error()


# =========================================================
# RECIPROCAL
# =========================================================

def reciprocal():

    try:

        number = get_current_number()

        if number == 0:
            raise ZeroDivisionError

        result = 1 / number

        show_result(
            f"1/{number}",
            result
        )

    except ZeroDivisionError:

        display.delete(0, tk.END)
        display.insert(0, "Can't divide by zero")

        clear_after_error()

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Invalid number")

        clear_after_error()


# =========================================================
# FACTORIAL
# =========================================================

def factorial():

    try:

        number = get_current_number()

        if number < 0 or number != int(number):
            raise ValueError

        result = math.factorial(int(number))

        show_result(
            f"{int(number)}!",
            result
        )

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Whole number only")

        clear_after_error()


# =========================================================
# PERCENTAGE
# =========================================================

def percentage():

    try:

        number = get_current_number()

        result = number / 100

        show_result(
            f"{number}%",
            result
        )

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Invalid number")

        clear_after_error()


# =========================================================
# TRIGONOMETRY HELPER
# =========================================================

def convert_angle(number):

    if angle_mode == "DEG":

        return math.radians(number)

    return number


# =========================================================
# SIN
# =========================================================

def sine():

    try:

        number = get_current_number()

        result = math.sin(
            convert_angle(number)
        )

        show_result(
            f"sin({number}°)" if angle_mode == "DEG"
            else f"sin({number})",
            result
        )

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Invalid number")

        clear_after_error()


# =========================================================
# COS
# =========================================================

def cosine():

    try:

        number = get_current_number()

        result = math.cos(
            convert_angle(number)
        )

        show_result(
            f"cos({number}°)" if angle_mode == "DEG"
            else f"cos({number})",
            result
        )

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Invalid number")

        clear_after_error()


# =========================================================
# TAN
# =========================================================

def tangent():

    try:

        number = get_current_number()

        result = math.tan(
            convert_angle(number)
        )

        show_result(
            f"tan({number}°)" if angle_mode == "DEG"
            else f"tan({number})",
            result
        )

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Invalid number")

        clear_after_error()


# =========================================================
# INVERSE SIN
# =========================================================

def inverse_sine():

    try:

        number = get_current_number()

        if number < -1 or number > 1:
            raise ValueError

        result = math.degrees(
            math.asin(number)
        )

        show_result(
            f"sin⁻¹({number})",
            result
        )

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Range: -1 to 1")

        clear_after_error()


# =========================================================
# INVERSE COS
# =========================================================

def inverse_cosine():

    try:

        number = get_current_number()

        if number < -1 or number > 1:
            raise ValueError

        result = math.degrees(
            math.acos(number)
        )

        show_result(
            f"cos⁻¹({number})",
            result
        )

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Range: -1 to 1")

        clear_after_error()


# =========================================================
# INVERSE TAN
# =========================================================

def inverse_tangent():

    try:

        number = get_current_number()

        result = math.degrees(
            math.atan(number)
        )

        show_result(
            f"tan⁻¹({number})",
            result
        )

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Invalid number")

        clear_after_error()


# =========================================================
# NATURAL LOG
# =========================================================

def natural_log():

    try:

        number = get_current_number()

        if number <= 0:
            raise ValueError

        result = math.log(number)

        show_result(
            f"ln({number})",
            result
        )

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Number must be > 0")

        clear_after_error()


# =========================================================
# LOG BASE 10
# =========================================================

def log10():

    try:

        number = get_current_number()

        if number <= 0:
            raise ValueError

        result = math.log10(number)

        show_result(
            f"log({number})",
            result
        )

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Number must be > 0")

        clear_after_error()


# =========================================================
# e TO THE POWER OF x
# =========================================================

def exponential():

    try:

        number = get_current_number()

        result = math.exp(number)

        show_result(
            f"e^{number}",
            result
        )

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Invalid number")

        clear_after_error()


# =========================================================
# 10 TO THE POWER OF x
# =========================================================

def ten_power():

    try:

        number = get_current_number()

        result = math.pow(10, number)

        show_result(
            f"10^{number}",
            result
        )

    except ValueError:

        display.delete(0, tk.END)
        display.insert(0, "Invalid number")

        clear_after_error()


# =========================================================
# PI
# =========================================================

def add_pi():

    add_to_display(math.pi)


# =========================================================
# EULER'S NUMBER
# =========================================================

def add_e():

    add_to_display(math.e)


# =========================================================
# DEG / RAD
# =========================================================

def toggle_angle_mode():

    global angle_mode

    if angle_mode == "DEG":

        angle_mode = "RAD"

    else:

        angle_mode = "DEG"

    angle_button.config(
        text=angle_mode
    )


# =========================================================
# CLEAR AFTER ERROR
# =========================================================

def clear_after_error():

    global current_expression

    current_expression = ""


# =========================================================
# HISTORY WINDOW
# =========================================================

def show_history():

    history_window = tk.Toplevel(root)

    history_window.title("Calculation History")
    history_window.geometry("450x450")

    if not history:

        tk.Label(
            history_window,
            text="No calculations yet.",
            font=("Arial", 14)
        ).pack(pady=20)

        return

    for number, calculation in enumerate(
        history,
        start=1
    ):

        tk.Label(
            history_window,
            text=f"{number}. {calculation}",
            font=("Arial", 11),
            anchor="w"
        ).pack(
            padx=15,
            pady=4,
            fill="x"
        )


# =========================================================
# SAVE HISTORY
# =========================================================

def save_history():

    if not history:

        display.delete(0, tk.END)
        display.insert(0, "No history")

        return

    try:

        with open(
            "calculation_history.txt",
            "w"
        ) as file:

            for calculation in history:

                file.write(
                    calculation + "\n"
                )

        display.delete(0, tk.END)
        display.insert(0, "History saved!")

    except OSError:

        display.delete(0, tk.END)
        display.insert(0, "Could not save")


# =========================================================
# SCIENTIFIC BUTTON FRAME
# =========================================================

scientific_frame = tk.Frame(root)

scientific_frame.pack(
    padx=10,
    pady=5,
    fill="x"
)


scientific_buttons = [

    ("sin", sine),
    ("cos", cosine),
    ("tan", tangent),
    ("sin⁻¹", inverse_sine),
    ("cos⁻¹", inverse_cosine),
    ("tan⁻¹", inverse_tangent),

    ("ln", natural_log),
    ("log", log10),
    ("eˣ", exponential),
    ("10ˣ", ten_power),
    ("√", square_root),
    ("x²", square),

    ("xʸ", power),
    ("1/x", reciprocal),
    ("n!", factorial),
    ("π", add_pi),
    ("e", add_e),
]


for index, (text, command) in enumerate(
    scientific_buttons
):

    button = tk.Button(
        scientific_frame,
        text=text,
        command=command,
        font=("Arial", 10)
    )

    button.grid(
        row=index // 6,
        column=index % 6,
        padx=2,
        pady=2,
        sticky="nsew"
    )


for column in range(6):

    scientific_frame.columnconfigure(
        column,
        weight=1
    )



# BASIC BUTTON FRAME


button_frame = tk.Frame(root)

button_frame.pack(
    padx=10,
    pady=10,
    fill="both",
    expand=True
)



# DEG/RAD BUTTON

angle_button = tk.Button(
    button_frame,
    text="DEG",
    command=toggle_angle_mode,
    font=("Arial", 12)
)

angle_button.grid(
    row=0,
    column=0,
    padx=4,
    pady=4,
    sticky="nsew"
)


# BASIC BUTTONS


buttons = [

    ("C", 0, 1, clear_display),
    ("⌫", 0, 2, delete_last),
    ("±", 0, 3, toggle_sign),
    ("%", 0, 4, percentage),

    ("(", 1, 0, lambda: add_to_display("(")),
    (")", 1, 1, lambda: add_to_display(")")),
    ("7", 1, 2, lambda: add_to_display("7")),
    ("8", 1, 3, lambda: add_to_display("8")),
    ("9", 1, 4, lambda: add_to_display("9")),

    ("÷", 2, 0, lambda: add_to_display("÷")),
    ("4", 2, 1, lambda: add_to_display("4")),
    ("5", 2, 2, lambda: add_to_display("5")),
    ("6", 2, 3, lambda: add_to_display("6")),
    ("×", 2, 4, lambda: add_to_display("×")),

    ("1", 3, 0, lambda: add_to_display("1")),
    ("2", 3, 1, lambda: add_to_display("2")),
    ("3", 3, 2, lambda: add_to_display("3")),
    ("-", 3, 3, lambda: add_to_display("-")),
    ("+", 3, 4, lambda: add_to_display("+")),

    ("0", 4, 0, lambda: add_to_display("0")),
    (".", 4, 1, lambda: add_to_display(".")),
    ("=", 4, 2, calculate),

    ("History", 4, 3, show_history),
    ("Save", 4, 4, save_history),
]


for text, row, column, command in buttons:

    button = tk.Button(
        button_frame,
        text=text,
        command=command,
        font=("Arial", 12)
    )

    button.grid(
        row=row,
        column=column,
        padx=4,
        pady=4,
        sticky="nsew"
    )


# Make basic buttons resize nicely

for row in range(5):

    button_frame.rowconfigure(
        row,
        weight=1
    )


for column in range(5):

    button_frame.columnconfigure(
        column,
        weight=1
    )
# START PROGRAM

root.mainloop()