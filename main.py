from tkinter import *

import pyautogui  # For some reason removing this screws the program resolution.
import requests
import pytemperature as pyt

import config_operations
import my_class

import time
import datetime


def on_closing():
    config_operations.write_todo(my_list)
    root.destroy()


def tick(clk):
    string = time.strftime('%H:%M:%S')
    clk.config(text=string)
    clk.after(1000, lambda: tick(clk))


def show_date(date_label):
    my_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    date_label.config(text=(datetime.date.today()).strftime("%d/%m/%y") + " - " + my_days[datetime.date.today().isoweekday() - 1])


def show_weather(weather_label):
    try:
        r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Ayd%C4%B1n,TR&APPID=1a605e94b1441e47b27482f8faee924c")
        data_json = r.json()
        temp = pyt.k2c(data_json["main"]["temp"])
        weather = data_json["weather"][0]["main"]
        weather_label.config(text=str(round(temp)) + "°C" + " - " + weather)
        weather_label.after(600000, lambda: show_weather(weather_label))
    except requests.exceptions.ConnectionError:
        weather_label.config(text="No internet connection")
        weather_label.after(600000, lambda: show_weather(weather_label))

#
#
my_dict = config_operations.read_cfg()
#
#
my_list = config_operations.read_todo()
if not my_list:
    my_list.append("[to-do]")
    my_list.append("[finished]")
#
#
root = Tk()
root.geometry("520x1000+1390+0")
root.title("PyAssistant")
root.configure(background="#21252B")

#
#
clock_date_frame = Frame(root, bg="#21252B", bd=4)
clock_date_frame.grid(row=0, column=0)
my_clock = Label(clock_date_frame, font=('calibri', 40, 'bold'), background="#2C313C", foreground="#0496d8")
my_clock.grid(row=0, column=0)
tick(my_clock)
#
my_date = Label(clock_date_frame, font=("calibri", 18), background="#2C313C", foreground="#0496d8")
my_date.grid(row=1, column=0, sticky=EW)  # NSEW fills
show_date(my_date)
#
my_weather = Label(clock_date_frame, font=("calibri", 15), background="#2C313C", foreground="#0496d8")
my_weather.grid(row=2, column=0, sticky=EW)
show_weather(my_weather)
#
#
checkbox_button_frame = Frame(root, bg="#21252B", bd=4)
checkbox_button_frame.grid(row=0, column=1)
#
#
hotspot_var = IntVar()
hotspot_checkbox = my_class.MyCheckButton("Open Mobile HotSpot", hotspot_var, "hotspot_var",
                                          checkbox_button_frame, 0, 4, W, my_dict)
#
hotspot_button = my_class.MyButton("Run", checkbox_button_frame, 0, 10, "hotspot")
#
#
gmail_var = IntVar()
gmail_checkbox = my_class.MyCheckButton("Open Gmail", gmail_var, "gmail_var",
                                        checkbox_button_frame, 1, 4, W, my_dict)
#
gmail_button = my_class.MyButton("Run", checkbox_button_frame, 1, 10, "gmail")
#
#
youtube_var = IntVar()
youtube_checkbox = my_class.MyCheckButton("Open YouTube", youtube_var, "youtube_var",
                                          checkbox_button_frame, 2, 4, W, my_dict)
#
youtube_button = my_class.MyButton("Run", checkbox_button_frame, 2, 10, "youtube")
#
#
spotify_var = IntVar()
spotify_checkbox = my_class.MyCheckButton("Open Spotify", spotify_var, "spotify_var",
                                          checkbox_button_frame, 3, 4, W, my_dict)
#
spotify_button = my_class.MyButton("Run", checkbox_button_frame, 3, 10, "spotify")
#
#
calendar_var = IntVar()
calendar_checkbox = my_class.MyCheckButton("Open Calendar", calendar_var, "calendar_var", checkbox_button_frame, 4, 4,
                                           W, my_dict)
#
calendar_button = my_class.MyButton("Run", checkbox_button_frame, 4, 10, "calendar")
#
#
calculator_var = IntVar()
calculator_checkbox = my_class.MyCheckButton("Open Calculator", calculator_var, "calculator_var", checkbox_button_frame,
                                             5, 4, W, my_dict)
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
to_do_frame.grid(row=1, column=0, columnspan=2)  # compared to root
to_do_title = Label(to_do_frame, font=30, background="#2C313C", foreground="#0496d8", text="TO-DO's",
                    width=25, height=2)
to_do_title.grid(row=0, column=0)  # compared to to_do_frame
#
#
to_do_list_frame = Frame(root, bg="#21252B", bd=4)
to_do_list_frame.grid(row=2, column=0, columnspan=2)
#
#
to_do_finished_list = Label(to_do_list_frame, font=30, background="#2C313C", foreground="#0496d8", text="FINISHED",
                            width=45, height=2)
to_do_finished_list.grid(row=100, column=1, pady=5)
#
#
todo_text_entry_var = StringVar()
todo_text_entry = my_class.MyTODOAdderButton(to_do_frame, to_do_list_frame, todo_text_entry_var, my_list)
#
#

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
