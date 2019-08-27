from tkinter import *
from tkinter import messagebox

import config_operations
import my_class

import time
import datetime


def tick(clk):
    string = time.strftime('%H:%M:%S')
    clk.config(text=string)
    clk.after(1000, lambda: tick(clk))


def show_date(date_label):
    date_label.config(text=(datetime.date.today()).strftime("%d/%m/%y"))


def show_day(day_label):
    my_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_label.config(text=my_days[datetime.date.today().isoweekday() - 1])
#
#
my_dict = config_operations.read_cfg()
print(my_dict)  # TODO: Remove this line later.
#
#
root = Tk()
root.geometry("515x800+200+200")
root.title("PyAssistant")
root.configure(background="#21252B")
# root.resizable(width=False, height=False)
#
#
clock_date_frame = Frame(root, bg="#21252B", bd=4)
clock_date_frame.grid(row=0, column=0)
my_clock = Label(clock_date_frame, font=('calibri', 40, 'bold'), background="#2C313C", foreground="#0496d8")
my_clock.grid(row=0, column=0)
tick(my_clock)
#
my_date = Label(clock_date_frame, font=("calibri", 20), background="#2C313C", foreground="#0496d8")
my_date.grid(row=1, column=0, sticky=EW)  # NSEW fills
show_date(my_date)
#
my_day = Label(clock_date_frame, font=("calibri", 15), background="#2C313C", foreground="#0496d8")
my_day.grid(row=2, column=0, sticky=EW)
show_day(my_day)
#
#
checkbox_button_frame = Frame(root, bg="#21252B", bd=4)
checkbox_button_frame.grid(row=0, column=1)
#
#
hotspot_var = IntVar()
hotspot_checkbox = my_class.MyCheckButton\
    ("Open Mobile HotSpot", hotspot_var, "hotspot_var", checkbox_button_frame, 0, 4, W, my_dict)
#
hotspot_button = my_class.MyButton("Run", checkbox_button_frame, 0, 10, "hotspot")
#
#
gmail_var = IntVar()
gmail_checkbox = my_class.MyCheckButton\
    ("Open Gmail", gmail_var, "gmail_var", checkbox_button_frame, 1, 4, W, my_dict)
#
gmail_button = my_class.MyButton("Run", checkbox_button_frame, 1, 10, "gmail")
#
#
youtube_var = IntVar()
youtube_checkbox = my_class.MyCheckButton\
    ("Open YouTube", youtube_var, "youtube_var", checkbox_button_frame, 2, 4, W, my_dict)
#
youtube_button = my_class.MyButton("Run", checkbox_button_frame, 2, 10, "youtube")
#
#
spotify_var = IntVar()
spotify_checkbox = my_class.MyCheckButton\
    ("Open Spotify", spotify_var, "spotify_var", checkbox_button_frame, 3, 4, W, my_dict)
#
spotify_button = my_class.MyButton("Run", checkbox_button_frame, 3, 10, "spotify")
#
#
calendar_var = IntVar()
calendar_checkbox = my_class.MyCheckButton("Open Calendar", calendar_var, "calendar_var", checkbox_button_frame, 4, 4, W, my_dict)
#
calendar_button = my_class.MyButton("Run", checkbox_button_frame, 4, 10, "calendar")
#
#
calculator_var = IntVar()
calculator_checkbox = my_class.MyCheckButton("Open Calculator", calculator_var, "calculator_var", checkbox_button_frame, 5, 4, W, my_dict)
#
calculator_button = my_class.MyButton("Run", checkbox_button_frame, 5, 10, "calculator")
#
# text, window, row, column, my_dict
execute_button = my_class.MyExecuteButton("Execute", clock_date_frame, 3, 0, my_dict)
#
#
save_config_button = Button(clock_date_frame, text="Save settings",
                            bg="#2C313C", fg="#0496d8", width="12",
                            activebackground="#2C313C", activeforeground="#0496d8",
                            command=lambda: config_operations.save_cfg(my_dict))
save_config_button.grid(row=3, column=0, sticky=E)
#
#
to_do_frame = Frame(root, bg="#2C313C", bd=4)
to_do_frame.grid(row=1, column=0)   # compared to root
to_do_title = Label(to_do_frame, font=20, background="#2C313C", foreground="#0496d8", text="TO-DO's")
to_do_title.grid(row=0, column=0, padx=75)
#
todo_text_entry_var = StringVar()
todo_text_entry = my_class.MyTODOAdderButton(to_do_frame, todo_text_entry_var, 1, 0)
#
#
to_do_finished_frame = Frame(root, bg="#2C313C", bd=4)
to_do_finished_frame.grid(row=1, column=1)  # compared to root
to_do_finished_title = Label(to_do_finished_frame, font=20, background="#2C313C", foreground="#0496d8", text="FINISHED")
to_do_finished_title.grid(row=0, column=1, padx=70)
#
to_do_finished_clear = my_class.MyFinishedClearButton(to_do_finished_frame, 1, 1)
#
#
root.mainloop()
