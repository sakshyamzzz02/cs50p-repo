def main():


    if validator("ENTER THE PASSWORD", "PASSWORD"):
        print("PASSWORD MATCHED, ACCESS GRANTED...")

    else:
        print("WRONG PASSSWORD, ACCESS DENIED!!!!")


def validator(user, password):
    name = input(user + ": ")
    return name == password

main()
