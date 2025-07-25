import math

def area_circle(radius, pi=math.pi):
    return round(pi* radius ** 2, 2)

def area_square(side):
    return side * side

def area_triangle(base, height=1):
    return 0.5 * base * height

def area_regular_polygon(n, side):
    if n < 3:
        return "Polygon must have at least 3 sides."
    area = (n * side ** 2) / (4 * math.tan(math.pi / n))
    return round(area, 2)

def print_menu():
    print("\nArea Calculator Menu")
    print("1. Area of Circle")
    print("2. Area of Square")
    print("3. Area of Triangle")
    print("4. Area of Regular n-sided Polygon")
    print("5. Exit")

# Menu loop
while True:
    print_menu()
    choice = input("Choose an option (1–5): ")

    if choice == "1":
        r = float(input("Enter the radius (cm): "))
        print("Area of Circle:", area_circle(r))

    elif choice == "2":
        s = float(input("Enter the side of the square (cm): "))
        print("Area of Square:", area_square(s))

    elif choice == "3":
        b = float(input("Enter the base of the triangle (cm): "))
        h_input = input("Enter the height (or press Enter for default 1)(cm): ")
        if h_input == "":
            print("Area of Triangle:", area_triangle(b))
        else:
            h = float(h_input)
            print("Area of Triangle:", area_triangle(b, h))

    elif choice == "4":
        n = int(input("Enter number of sides (n): "))
        a = float(input("Enter length of each side (cm): "))
        print("Area of Regular Polygon:", area_regular_polygon(n, a))

    elif choice == "5":
        print("Exiting..")
        break

    else:
        print("Invalid choice. Please select between 1–5.")