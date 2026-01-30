import tkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable(False, False)

# timer heading
timer_heading = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_heading.grid(row=0, column=1)

# create canvas for the image
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato_img)
canvas.create_text(108, 138, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

# start and reset button
start_button = tkinter.Button(text="Start")
start_button.grid(row=2, column=0, padx=20, pady=20)

start_button = tkinter.Button(text="Reset")
start_button.grid(row=2, column=2, padx=20, pady=20)

# checkmark button
checkmark = tkinter.Label(text="✔", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
checkmark.grid(row=3, column=1)

# keep windown open
window.mainloop()
