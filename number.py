while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not a number")

print(f"x is {x}")