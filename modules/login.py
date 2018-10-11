def create_file(file_name) :
    with open(file_name, "w") as new_file :
        if file_name == "account.txt":
            account_dict = {"username": [], "password": []}
            new_file.write("{}".format(account_dict))

def check_existing_account() :
    try :
        with open("account.txt", "r") as pull_file :
            existing_account_dict = eval(pull_file.read())
        return existing_account_dict
    except :
        create_file("account.txt")
        with open("account.txt", "r") as pull_file :
            existing_account_dict = eval(pull_file.read())
        return existing_account_dict

def create_account(existing_account_dict) :
    existing_account_dict["username"].append(create_username)
    existing_account_dict["password"].append(create_password)

    with open("account.txt", "w") as out_file :
        out_file.write("{}".format(existing_account_dict))

def login(input_username, input_password) :
    existing_account_dict = check_existing_account()

    username = input_username.get()
    password = input_password.get()

    index = existing_account_dict["username"].index(username)

    if (username in existing_account_dict["username"] and password == existing_account_dict["password"][index]):
        print("Authorized")
    else :
        print("Fail")
