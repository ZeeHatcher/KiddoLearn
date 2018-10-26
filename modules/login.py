accounts = r"data\accounts.txt"

def create_file(file_name) :
    with open(file_name, "w") as new_file :
        if file_name == accounts:
            account_dict = {"username": [], "password": []}
            new_file.write("{}".format(account_dict))

def check_file(file_name) :
    with open(file_name, "r") as pull_file :
        f = eval(pull_file.read())
    return f

def create_account(entry_username, entry_password) :
    existing_account_dict = check_file(accounts)

    existing_account_dict["username"].append(entry_username)
    existing_account_dict["password"].append(entry_password)

    with open(accounts, "w") as out_file :
        out_file.write("{}".format(existing_account_dict))

def login(entry_username, entry_password) :
    existing_account_dict = check_file(accounts)

    username = entry_username.get()
    password = entry_password.get()

    if (username in existing_account_dict["username"]) :
      index = existing_account_dict["username"].index(username)
      if (password == existing_account_dict["password"][index]) :
        authorized = True
      else :
        authorized = False
    else :
      authorized = False

    return authorized
