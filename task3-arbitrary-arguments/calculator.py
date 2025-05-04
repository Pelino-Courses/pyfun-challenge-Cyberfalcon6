def calculate(*args, **kwargs):
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("All positional arguments must be numbers.")
    if not all(isinstance(value, bool) for value in kwargs.values()):
        raise TypeError("All keyword argument values must be boolean.")

    result = args[0] if args else 0

    if kwargs.get("add", False):
        result = sum(args)
    if kwargs.get("multiply", False):
        result = 1
        for num in args:
            result *= num
    if kwargs.get("subtract", False):
        result = args[0] - sum(args[1:])
    if kwargs.get("divide", False):
        for num in args[1:]:
            if num == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result /= num

    return result

if __name__ == "__main__":
    try:
        numbers = input("Enter numbers separated by spaces: ").split()
        numbers = [float(num) for num in numbers]
        operation = input("Enter operation (add, multiply, subtract, divide): ").strip().lower()
        operations = {operation: True}
        print("Result:", calculate(*numbers, **operations))
    except Exception as e:
        print(f"Error: {e}")