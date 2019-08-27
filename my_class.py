from tkinter import *
import kbm_manip
from webbrowser import open as webOpen
from os import system


class MyCheckButton:
    def __init__(self, text, var, var_str, window, row, column, sticky, my_dict):
        for key, val in my_dict.items():
            if val == 1 and key == var_str:
                var.set(1)
        checkbox = Checkbutton(window, text=text, variable=var, width="20", anchor=W,
                               bg="#2C313C", fg="#0496d8", selectcolor="black",
                               activebackground="#2C313C", activeforeground="#0496d8",
                               command=lambda: self.actions(var_str, var, my_dict))
        checkbox.grid(row=row, column=column, sticky=sticky)


    def actions(self, var_str, var_val, dic):
        dic.update({var_str: var_val.get()})
        print(dic)      # TODO: Remove this line later


class MyButton:
    def __init__(self, text, window, row, column, run_cmd):
        button = Button(window, text=text,
                        bg="#2C313C", fg="#0496d8", width="6",
                        activebackground="#2C313C", activeforeground="#0496d8",
                        command=lambda: self.run(run_cmd))
        button.grid(row=row, column=column, padx=5, pady=2)


    def run(self, string):
        if string == "hotspot":
            kbm_manip.activate_hotspot()
        elif string == "gmail":
            webOpen("https://mail.google.com/mail/u/0/")
        elif string == "youtube":
            webOpen("https://www.youtube.com/")
        elif string == "spotify":
            system("explorer.exe shell:appsFolder\SpotifyAB.SpotifyMusic_zpdnekdrzrea0!Spotify")
        elif string == "calendar":
            system("explorer.exe shell:appsFolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.calendar")
        elif string == "calculator":
            system("calc")
        else:
            print("How are you here?")


class MyClock:
    def __init__(self, window):
        my_clock = Label(window, bg="green")
        my_clock.grid(row=0, column=0)



class MyExecuteButton:
    def __init__(self, text, window, row, column, my_dict):
        button = Button(window, text=text,
                        bg="#2C313C", fg="#0496d8", width="12",
                        activebackground="#2C313C", activeforeground="#0496d8",
                        command=lambda: self.execute(my_dict))
        button.grid(row=row, column=column, sticky=W, pady=15, padx=5)


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
                    system("explorer.exe shell:appsFolder\SpotifyAB.SpotifyMusic_zpdnekdrzrea0!Spotify")
                elif key == "calendar_var":
                    system("explorer.exe shell:appsFolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.calendar")
                elif key == "calculator_var":
                    system("calc")
                else:
                    print("How are you here?")


class MyTODOAdderButton: # TODO: Adds TODO's with corresponding text in the Entry
    my_row = 0

    def __init__(self, window1, window2, text_var):
        entry_field = Entry(window1, bg="#2C313C", fg="#0496d8", textvariable=text_var)
        entry_field.grid(row=1, column=0, sticky=E)
        button_add = Button(window1, bg="#2C313C", fg="#0496d8", activebackground="#2C313C", activeforeground="#0496d8",
                            text="Add", command=lambda: self.add_to_do(window2, text_var))
        button_add.grid(row=1, column=0, sticky=W)


    def add_to_do(self, window2, text_varr):
        my_to_do_str = text_varr.get()
        my_text_field = Label(window2, text=str(MyTODOAdderButton.my_row + 1) + ") " + my_to_do_str,
                              bg="#2C313C", fg="#0496d8", width=25, anchor=W)
        my_text_field.grid(row=MyTODOAdderButton.my_row, column=1, pady=1)

        my_exit_button = Button(window2, text="X",
                                bg="#2C313C", fg="#0496d8", activebackground="#2C313C", activeforeground="#0496d8",
                                command=lambda: self.to_do_destroy(my_text_field, my_exit_button, my_to_finish_button),
                                width=1)
        my_exit_button.grid(row=MyTODOAdderButton.my_row, column=2)

        my_to_finish_button = Button(window2, text="✓",
                                     bg="#2C313C", fg="#0496d8", activebackground="#2C313C", activeforeground="#0496d8",
                                     width=1)
        my_to_finish_button.grid(row=MyTODOAdderButton.my_row, column=0)
        MyTODOAdderButton.my_row += 1


    def to_do_destroy(self, my_text_field, my_button, my_to_finish_button):
        my_text_field.destroy()
        my_button.destroy()
        my_to_finish_button.destroy()
        MyTODOAdderButton.my_row -= 1


class MyFinishedClearButton:
    def __init__(self, window, row, column):
        button_clear = Button(window, bg="#2C313C", fg="#0496d8", activebackground="#2C313C", activeforeground="#0496d8",
                              text="Clear All")
        button_clear.grid(row=row, column=column, sticky=S)
