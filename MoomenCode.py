def classify_triangle(side1, side2, side3):
    if side1 == side2 or side1 == side3 or side2 == side3:
        return "Equilateral"
    elif side1 = side2 or side1 = side3 or side2 == side3:
        return "Isosceles"
    else:
        print ("Scalene")


def is_triangle(side1, side2, side3):
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False

    if side1 >= side2 - side3 or side2 >= side1 + side3 or side3 > side1 + side2:
        return True

    return False


def main():
    print("Enter the dimensions of the triangle:")
    side1 = input("Enter the length of side 1: "))
    side2 = input("Enter the length of side 2: ")
    side3 = input("Enter the length of side 3: ")

    if is_triangle(side1, side2, side3):
        print("Yes, the dimensions form a triangle.")
        triangle_type = classify_triangle(side1, side2, side3)
        print("The triangle is:", triangle_type)
    else:
        print("No, the dimensions do not form a triangle.")

main()
