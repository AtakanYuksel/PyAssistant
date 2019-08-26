from tkinter import *
import kbm_manip
from webbrowser import open as webOpen
from os import system


class MyCheckButton:
    def __init__(self, text, var, var_str, window, row, column, sticky, my_dict):
        for key, val in my_dict.items():
            if val == 1 and key == var_str:
                var.set(1)
        checkbox = Checkbutton(window, text=text, variable=var, width="20",
                               bg="#2C313C", fg="#0496d8", selectcolor="black",
                               activebackground="#2C313C", activeforeground="#0496d8",
                               command=lambda: self.actions(var_str, var, my_dict))\
            .grid(row=row, column=column, sticky=sticky)


    def actions(self, var_str, var_val, dic):
        dic.update({var_str: var_val.get()})
        print(dic)      # remove later


class MyButton:
    def __init__(self, text, window, row, column, run_cmd):
        button = Button(window, text=text,
                        bg="#2C313C", fg="#0496d8", width="12",
                        activebackground="#2C313C", activeforeground="#0496d8",
                        command=lambda: self.run(run_cmd))\
        .grid(row=row, column=column, padx=5, pady=2)


    def run(self, string):
        if string == "hotspot":
            kbm_manip.activate_hotspot()
        elif string == "gmail":
            webOpen("https://mail.google.com/mail/u/0/")
        elif string == "youtube":
            webOpen("https://www.youtube.com/")
        elif string == "spotify":
            webOpen("https://www.spotify.com/")
        elif string == "calendar":
            system("explorer.exe shell:appsFolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.calendar")
        elif string == "calculator":
            system("calc")
        else:
            print("How are you here?")


class myClock:
    def __init__(self, window):
        my_clock = Label(window, bg="green")
        my_clock.grid(row=0, column=0)



class MyExecuteButton:
    def __init__(self, text, window, row, column, my_dict):
        button = Button(window, text=text,
                        bg="#2C313C", fg="#0496d8", width="12",
                        activebackground="#2C313C", activeforeground="#0496d8",
                        command=lambda: self.execute(my_dict))\
            .grid(row=row, column=column, pady=15)


    def execute(self, dic):
        for key, value in dic.items():
            if value == 1:
                if key == "hotspot_var":
                    kbm_manip.activate_hotspot()
                elif key == "gmail_var":
                    webOpen("https://mail.google.com/mail/u/0/")
                elif key == "youtube_var":
                    webOpen("https://www.youtube.com/")
                elif key == "spotify_var":
                    webOpen("https://www.spotify.com/")
                elif key == "calendar_var":
                    system("explorer.exe shell:appsFolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.calendar")
                elif key == "calculator_var":
                    system("calc")
                else:
                    print("How are you here?")
