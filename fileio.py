# Constants for color, size, fonts, etc.
SUBMIT = "#81ff42"
SUBMIT_D = "#5fc12e"
MISC = "#c4faff"
MISC_D = "#99c5c9"
SPECIAL = "#fff189"
SPECIAL_D = "#d1c56e"
CANCEL = "#ff7663"
CANCEL_D= "#c65c4d"
H1 = "Verdana 16 bold"
H2 = "Verdana 12 bold"
DESC = "Verdana 30"
MINI = "300x300+500+250"
MEDIUM = "500x500+500+250"
LARGE = "800x600+250+250"

accounts = r"data\accounts.txt"

def format_txt(name):
    f = "data\\" + name + ".txt"
    return f

def create_file(file_name):
    with open(file_name, "w") as new_file:
        new_file.write("")

def check_file(file_name):
    with open(file_name, "r") as pull_file:
        cont = pull_file.readlines()
        f = []

        for line in cont:
            c = eval(line)
            f.append(c)

    return f

def format_gif(folder, gif):
    f = "images\\lessons\\" + folder + "\\" + gif

    return f

def check_description(lesson):
    desc_file = "txt_files\\lesson\\" + lesson + ".txt"

    with open(desc_file, "r") as f:
        cont = f.readlines()
        descriptions = []

        for line in cont:
            desc = eval(line)
            descriptions.append(desc)

    return descriptions

def check_exercise(lesson):
    ex_file = "txt_files\\exercise\\" + lesson + ".txt"

    with open(ex_file, "r") as f:
        cont = f.readlines()
        exercises = []

        for line in cont:
            ex = eval(line)
            exercises.append(ex)

    return exercises
