from shapes import Circle, Rectangle, Triangle

def main():
    try:
        circle = Circle(7)
        rectangle = Rectangle(5, 10)
        triangle = Triangle(6, 8)

        shapes = [circle, rectangle, triangle]

        for shape in shapes:
            print(shape)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()