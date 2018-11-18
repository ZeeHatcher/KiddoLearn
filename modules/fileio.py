accounts = r"data\accounts.txt"


def format_txt(name):
    f = "data\\" + name + ".txt"
    return f

def create_file(file_name):
    with open(file_name, "w") as new_file:
        new_file.write("[]")

def check_file(file_name):
    with open(file_name, "r") as pull_file:
        f = eval(pull_file.read())
    return f

def format_gif(folder, gif):
    f = "images\\lessons\\" + folder + "\\" + gif

    return f

def check_description(lesson):
    desc_file = "modules\\descriptions\\" + lesson + ".txt"

    with open(desc_file, "r") as f:
        cont = f.readlines()
        descriptions = []

        for line in cont:
            desc = eval(line)
            descriptions.append(desc)

    return descriptions
