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

def create_account(existing_account_dict) :
    existing_account_dict["username"].append(create_username)
    existing_account_dict["password"].append(create_password)

    with open("account.txt", "w") as out_file :
        out_file.write("{}".format(existing_account_dict))

def login(input_username, input_password, frame) :
    existing_account_dict = check_file("account.txt")

    username = input_username.get()
    password = input_password.get()

    if (username in existing_account_dict["username"]) :
      index = existing_account_dict["username"].index(username)
      if (password == existing_account_dict["password"][index]) :
        print("Authorized")
        show(frame)
      else :
        print("Please enter a correct password")
    else :
      print("Username not found")
        