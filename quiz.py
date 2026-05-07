def main():

    score = 0
    if quiz("Capital city of Nepal", "Kathmandu"):
        score += 1

    print(score)

def quiz(Q, ans):
    user = input(Q + ":")

    return user.lower().strip() == ans.lower()

main()
