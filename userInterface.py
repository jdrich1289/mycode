print("Hello")

sayagain = "y"


while sayagain == "y":
    sayagain = input("Say hello again? (y/n): ").lower()
    if sayagain == "y":
        print("Hello")
    else:
        print("Bye!")
