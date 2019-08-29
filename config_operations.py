from tkinter import messagebox


def read_cfg():
    my_dict = {}
    try:
        config_file = open("config.txt", "r")  # try to open the file
        for a_line in config_file:
            (key, val) = a_line.split(" : ")
            my_dict[key] = int(val.strip())
        config_file.close()
    except FileNotFoundError:   # create/reset the file if it does not exist or is corrupt
        open("config.txt", "w")
    return my_dict


def save_cfg(my_dict):
    config_file = open("config.txt", "w")   # save to the file
    for key, val in my_dict.items():
        config_file.write(str(key) + " : " + str(val) + "\n")
    config_file.close()
    messagebox.showinfo("Info", "Saved successfully.")


def read_todo():
    my_list = []
    try:
        to_do = open("todo.txt", "r")
        for a_line in to_do:
            my_list.append(a_line.strip())
    except FileNotFoundError:   # create/reset the file if it does not exist or is corrupt.
        to_do = open("todo.txt", "w")
        to_do.write("[to-do]")
        to_do.write("[finished]")
    return my_list


def write_todo(my_list):
    to_do = open("todo.txt", "w")
    for a_line in my_list:
        to_do.write(a_line + "\n")
