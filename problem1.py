# GCD
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)

# LCM


def LCM(a, b):
    return (a * b) // GCD(a, b)

# you can do magic by america


def matulog():
    while True:
        try:
            x = int(input("Enter a value for x: "))
            y = int(input("Enter a value for y: "))

            if x <= 0 or y <= 0:
                print(
                    "Please enter positive integers only (no zero or negative values). Please try again.\n")
                continue

            print(f"The LCM of {x} and {y} is = {LCM(x, y)}")
            break

        except ValueError:
            print("Invalid input!! Please enter integer values.\n")


# activation center
matulog()
