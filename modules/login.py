def create_file(file_name) :
    with open(file_name, "w") as new_file :
        if file_name == "account.txt":
            account_dict = {"username": [], "password": []}
            new_file.write("{}".format(account_dict))

def check_file(file_name) :
    try :
        with open(file_name, "r") as pull_file :
            f = eval(pull_file.read())
        return f
    except :
        create_file(file_name)
        with open(file_name, "r") as pull_file :
            f = eval(pull_file.read())
        return f

def show(frame) :
  frame.lift()

def create_account(entry_username, entry_password) :
    existing_account_dict = check_file("account.txt")

    existing_account_dict["username"].append(entry_username)
    existing_account_dict["password"].append(entry_password)

    with open("account.txt", "w") as out_file :
        out_file.write("{}".format(existing_account_dict))

def login(entry_username, entry_password, frame) :
    existing_account_dict = check_file("account.txt")

    username = entry_username.get()
    password = entry_password.get()

    if (username in existing_account_dict["username"]) :
      index = existing_account_dict["username"].index(username)
      if (password == existing_account_dict["password"][index]) :
        print("Authorized")
        show(frame)
      else :
        print("Please enter a correct password")
    else :
      print("Username not found")
