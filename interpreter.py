# for the format 100+1, 1*2...
expression = input("Expressions: ")
x, y, z = expression.split()
x = float(x)
z = float(z)
match y:
    case "+":
        print(f"{x+z:.1f}")
    case "-":
        print(f"{x-z:.1f}")
    case "*":
        print(f"{x*z:.1f}")
    case "/":
        if z == 0:
            print("Error: Division by Zero")
        else:
            print(f"{x/z:.1f}")
    case _:
        print("Use a valid operator")

