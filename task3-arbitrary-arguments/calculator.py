def calculate(*args, **kwargs):
    """
    Applies given operation(addition, multiplication, etc) to a number of arguments
    Args:
      args*(int, float): floating point numbers of any number
      add(bool): will return sum of args* if set to True
      multiply(bool): will return product of all args if True
      divide(bool): divides the args if set to True
      subtract(bool): subtract the args if set to True
    """
    # Check if all positional arguments are numbers (int or float)
    if not all(isinstance(arg, (int, float)) for arg in args):
        raise TypeError("All positional arguments must be numbers.")
    if not all(isinstance(value, bool) for value in kwargs.values()):
        raise TypeError("All keyword argument values must be boolean.")

    if not args:
        raise ValueError("At least one number must be provided.")

    if not any(kwargs.values()):
        raise ValueError("At least one operation (add, multiply, subtract, divide) must be specified.")

    result = args[0]

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
        if operation not in {"add", "multiply", "subtract", "divide"}:
            raise ValueError(f"Unsupported operation: {operation}")
        operations = {operation: True}
        print("Result:", calculate(*numbers, **operations))
    except Exception as e:
        print(f"Error: {e}")