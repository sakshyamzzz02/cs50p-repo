greet = input("How would you greet the costumer: ")
greet = greet.lower().strip()
First = greet.split(" ")
if First[0] == "hello" or First[0] == "hello,":
    print("$0")
elif greet[0] == "h":
    print("$20")
else:
    print("$100")
