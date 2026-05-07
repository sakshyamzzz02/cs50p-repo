NPR = float(input("enter the NPR amount: "))
C = input("enter the commision percentage: ")
C = float(C.replace("%", "")) / 100
USD = NPR / 141 - (NPR / 141 * C)
print(f"the exchanged USD amount is: ${USD}")
