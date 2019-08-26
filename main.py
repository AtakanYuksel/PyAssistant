from tkinter import *
from tkinter import messagebox

import config_operations
import my_class

import time
#
#
def tick(clk):
    string = time.strftime('%H:%M:%S')
    clk.config(text=string)
    clk.after(1000, lambda: tick(clk))
#
#
my_dict = config_operations.read_cfg() #anan
print(my_dict)
#
#
root = Tk()
root.geometry("800x600+0+0")
root.title("PyAssistant")
root.configure(background="#21252B")
# root.resizable(width=False, height=False)
#
#
clock_frame = Frame(root)
clock_frame.grid(row=0, column=0)
my_clock = Label(clock_frame, font=('calibri', 40, 'bold'), background="#2C313C", foreground="#0496d8")
my_clock.grid(row=0, column=0)
tick(my_clock)
#
#
checkbox_button_frame = Frame(root, bg="#21252B", bd=8)
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
execute_button = my_class.MyExecuteButton\
    ("Execute", root, 10, 0, my_dict)
#
#
save_config_button = Button(root, text="Save settings",
                            bg="#2C313C", fg="#0496d8", width="12",
                            activebackground="#2C313C", activeforeground="#0496d8",
                            command=lambda: config_operations.save_cfg(my_dict)).grid(row=11, column=0)
#
#
root.mainloop()
# TO-DO
# move execute-save settings to bottom.

