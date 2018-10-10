def create_account(existing_account) :
    create_username = input("Enter your username: ")
    create_password = input("Enter your password: ")

    existing_account["username"].append(create_username)
    existing_account["password"].append(create_password)

    with open("data.txt", "w") as out_file :
        out_file.write("{}".format(existing_account))

def create_account_prompt(existing_account) :
    prompt = input("Existing account found. Create new account? (Y/N) : ")

    if prompt.upper() == "Y" :
        create_account(existing_account)
    elif prompt.upper() == "N" :
        login()
    else :
        print("Please give a correct input...")
        create_account_prompt(existing_account)

def check_existing_account() :
    with open("data.txt", "r") as pull_file :
        existing_account = eval(pull_file.read())

    if len(existing_account["username"]) == 0 :
        create_account(existing_account)
    else :
        create_account_prompt(existing_account)

check_existing_account()
