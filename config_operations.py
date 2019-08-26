from tkinter import messagebox


def read_cfg():
    my_dict = {}
    try:
        config_file = open("config.txt", "r+")
        for a_line in config_file:
            (key, val) = a_line.split(" : ")
            my_dict[key] = int(val.strip())
        config_file.close()
    except FileNotFoundError:
        open("config.txt", "w")
    return my_dict


def save_cfg(my_dict):
    try:
        config_file = open("config.txt", "w")
        for key, val in my_dict.items():
            config_file.write(str(key) + " : " + str(val) + "\n")
        config_file.close()
        messagebox.showinfo("Info", "Saved successfully.")
    except:
        exit(-1)
