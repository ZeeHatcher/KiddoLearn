accounts = r"C:\Users\Jw Lim\Python\kiddo_learn-master\data\accounts.txt" #I've changed the last few lines to use this location, like the "Creds" thingy in my login_module

def format_txt(name):
    f = r"C:\Users\Jw Lim\Python\kiddo_learn-master\data\\" + name + ".txt" #whereas this one creates a new profile
    return f

def create_file(file_name):
    with open(file_name, "w") as new_file:
        new_file.write("[]")

def check_file(file_name):
    with open(file_name, "r") as pull_file:
        f = eval(pull_file.read())
    return f

def create_account(entry_username, entry_password):
    new_account = {"username": entry_username, "password": entry_password}
    existing_accounts = check_file(accounts)

    existing_accounts.append(new_account)

    with open(accounts, "w") as out_file:
        out_file.write("{}".format(existing_accounts))

def login(entry_username, entry_password):
    authorized = False
    existing_accounts = check_file(accounts)

    username = entry_username.get()
    password = entry_password.get()

    for account in existing_accounts:
        if username == account["username"] and password == account["password"]:
            authorized = True
            break
        else:
            continue

    return authorized
