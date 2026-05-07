answer = input("What is the answer to the great question of the life? ")
# remove the space to the left and right and lowercasing..
answer = answer.lower().strip()
# checking  the universal truth
if(answer == "42" or answer == "forty-two" or answer == "forty two"):
    print("Yes")
else:
    print("No")

