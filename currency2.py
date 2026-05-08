#take input and call the functions
def main():
    NPR = in_float(input("enter the NPR amount: "))
    Comission = num(input("Enter the comission percentage: "))
    USD = NPR / 141 - ( NPR / 141 * Comission)
    print(f"The exchanged currency in USD is: $ {USD}")

#currency into float and eliminating the string part(NPR)
def in_float(N):
    return float(N.replace("NPR", ""))

def num(C):
    return float(C.replace("%","")) / 100

main()


