from math import sqrt


# Quadratic formula
def solve(a, b, c):
    d = (b ** 2) - (4 * a * c)
    if d >= 0:
        return (-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)
    return False


def main():
    a = float(input("number a >>"))
    b = float(input("number b >>"))
    c = float(input("number c >>"))

    # Calculate the values of x
    answer = solve(a, b, c)
    # Show results
    if answer:
        if answer[0] == answer[1]:
            print(f"x = {answer[0]}")
        else:
            print(f"x = {answer[0]}; x = {answer[1]}")
    else:
        # Can't get the square root of a negative number
        print("Solucion imaginaria")


if __name__ == "__main__":
    main()
