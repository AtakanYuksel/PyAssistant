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


class MyButton:
    def __init__(self, text, window, row, column, run_cmd):
        button = Button(window, text=text,
                        bg="#2C313C", fg="#0496d8", width="6",
                        activebackground="#2C313C", activeforeground="#0496d8",
                        command=lambda: self.run(run_cmd))
        button.grid(row=row, column=column, padx=5, pady=2)

    def run(self, string):
        if string == "hotspot":
            system("PowerShell.exe -ExecutionPolicy Bypass -Command \" & \'C:\\Users\\Atakan\\Desktop\\tkinter\\hotspot.ps1\'\"")
        elif string == "gmail":
            webOpen("https://mail.google.com/mail/u/0/")
        elif string == "youtube":
            webOpen("https://www.youtube.com/")
        elif string == "spotify":
            system(r"explorer.exe shell:appsFolder\
            SpotifyAB.SpotifyMusic_zpdnekdrzrea0!Spotify")
        elif string == "calendar":
            system(r"explorer.exe shell:appsFolder\
            microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.calendar")
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
                    system("PowerShell.exe -ExecutionPolicy Bypass -Command \" & \'C:\\Users\\Atakan\\Desktop\\hotspot.ps1\'\"")
                elif key == "gmail_var":
                    webOpen("https://mail.google.com/mail/u/0/")
                elif key == "youtube_var":
                    webOpen("https://www.youtube.com/")
                elif key == "spotify_var":
                    system(r"explorer.exe shell:appsFolder\SpotifyAB.SpotifyMusic_zpdnekdrzrea0!Spotify")
                elif key == "calendar_var":
                    system(
                        r"explorer.exe shell:appsFolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.calendar")
                elif key == "calculator_var":
                    system("calc")
                else:
                    print("How are you here?")


class MyTODOAdderButton:
    my_row = 0

    my_finished_row = 150

    def __init__(self, to_do_frame, to_do_list_frame, text_var, my_list):
        entry_field = Entry(to_do_frame, bg="#2C313C", fg="#0496d8", textvariable=text_var)
        entry_field.grid(row=0, column=1, padx=5)
        button_add = Button(to_do_frame, bg="#2C313C", fg="#0496d8", activebackground="#2C313C",
                            activeforeground="#0496d8",
                            text="Add", command=lambda: self.add_to_do(to_do_list_frame, text_var, 0, my_list, 1))
        button_add.grid(row=0, column=2)
        self.preset_todos_finished(to_do_list_frame, my_list)

    def preset_todos_finished(self, to_do_list_frame, my_list):
        my_line = StringVar()
        if my_list:
            for i in my_list[1:]:
                if i != "[finished]":
                    my_line.set(i)
                    self.add_to_do(to_do_list_frame, my_line, 0, my_list, 0)
                else:
                    for j in my_list[my_list.index(i) + 1:]:
                        my_line.set(j)
                        self.add_to_do(to_do_list_frame, my_line, 1, my_list, 0)
                    break

    def add_to_do(self, to_do_list_frame, text_var, finish_flag, my_list, after_flag):
        my_to_do_str = text_var.get()
        text_var.set("")
        my_text_field = Label(to_do_list_frame, text="- " + my_to_do_str,
                              bg="#2C313C", fg="#0496d8", width=50, anchor=W)
        my_text_field.grid(row=MyTODOAdderButton.my_row, column=1, pady=1)

        my_remove_button = Button(to_do_list_frame, text=chr(9587),
                                  bg="#2C313C", fg="#0496d8", activebackground="#2C313C", activeforeground="#0496d8",
                                  command=lambda: self.to_do_destroy(my_text_field, my_remove_button,
                                                                     my_to_finish_button, my_to_do_str, my_list),
                                  width=3, height=1)
        my_remove_button.grid(row=MyTODOAdderButton.my_row, column=1, sticky=E)

        my_to_finish_button = Button(to_do_list_frame, text=chr(10003),
                                     bg="#2C313C", fg="#0496d8", activebackground="#2C313C", activeforeground="#0496d8",
                                     command=lambda: self.move_to_finished(to_do_list_frame, my_text_field,
                                                                           my_remove_button, my_to_finish_button, my_to_do_str, my_list, 1),
                                     width=3, height=1)
        my_to_finish_button.grid(row=MyTODOAdderButton.my_row, column=1, sticky=W)

        if finish_flag == 1:
            self.move_to_finished(to_do_list_frame, my_text_field, my_remove_button, my_to_finish_button, my_to_do_str, my_list, 0)

        if after_flag == 1:
            my_list.insert(my_list.index("[finished]"), my_to_do_str)
        MyTODOAdderButton.my_row += 1

    def to_do_destroy(self, my_text_field, my_button, my_to_finish_button, text_var, my_list):
        my_text_field.destroy()
        my_button.destroy()
        my_to_finish_button.destroy()

        my_list.remove(text_var)

    def move_to_finished(self, to_do_list_frame, my_text_field, my_button, my_to_finish_button, text_var, my_list, after_flag):
        my_text_field.grid_forget()
        my_button.destroy()
        my_to_finish_button.destroy()

        my_text_field.grid(row=MyTODOAdderButton.my_finished_row, column=1, pady=1)

        remove_from_finished_button = Button(to_do_list_frame, text=chr(9587),
                                             bg="#2C313C", fg="#0496d8", activebackground="#2C313C",
                                             activeforeground="#0496d8",
                                             command=lambda: self.to_do_destroy(my_text_field,
                                                                                remove_from_finished_button,
                                                                                back_to_to_do_button, text_var, my_list),
                                             width=3, height=1)
        remove_from_finished_button.grid(row=MyTODOAdderButton.my_finished_row, column=1, sticky=E)

        back_to_to_do_button = Button(to_do_list_frame, text=chr(9100),
                                      bg="#2C313C", fg="#0496d8", activebackground="#2C313C",
                                      activeforeground="#0496d8",
                                      command=lambda: self.back_to_to_do(to_do_list_frame, my_text_field,
                                                                         remove_from_finished_button,
                                                                         back_to_to_do_button, text_var, my_list, 1),
                                      width=3, height=1)
        back_to_to_do_button.grid(row=MyTODOAdderButton.my_finished_row, column=1, sticky=W)

        if after_flag == 1:
            my_list.append(text_var)
            my_list.remove(text_var)

        MyTODOAdderButton.my_finished_row += 1

    def back_to_to_do(self, to_do_list_frame, my_text_field, remove_from_finished_button, back_to_to_do_button, text_var, my_list, after_flag):
        remove_from_finished_button.destroy()
        back_to_to_do_button.destroy()

        my_text_field.grid_forget()
        my_text_field.grid(row=MyTODOAdderButton.my_row, column=1)

        my_new_remove_button = Button(to_do_list_frame, text=chr(9587),
                                      bg="#2C313C", fg="#0496d8", activebackground="#2C313C",
                                      activeforeground="#0496d8",
                                      command=lambda: self.to_do_destroy(my_text_field, my_new_remove_button,
                                                                         my_new_to_finish_button, text_var, my_list),
                                      width=3, height=1)
        my_new_remove_button.grid(row=MyTODOAdderButton.my_row, column=2)

        my_new_to_finish_button = Button(to_do_list_frame, text=chr(10003),
                                         bg="#2C313C", fg="#0496d8", activebackground="#2C313C",
                                         activeforeground="#0496d8",
                                         command=lambda: self.move_to_finished(to_do_list_frame, my_text_field,
                                                                               my_new_remove_button,
                                                                               my_new_to_finish_button, text_var, my_list, 0),
                                         width=3, height=1)
        my_new_to_finish_button.grid(row=MyTODOAdderButton.my_row, column=0)

        if after_flag == 1:
            my_list.remove(text_var)
            my_list.insert(my_list.index("[finished]"), text_var)

        MyTODOAdderButton.my_row += 1