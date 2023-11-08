import ast

def find_machine_epsilon(float_type=float):
    machine_epsilon = float_type(1.0)
    while float_type(1.0) + machine_epsilon != 1.0:
        machine_epsilon /= 2.0
    return machine_epsilon * 2.0

def safe_eval(expr):
    try:
        # Attempt to parse the expression to an Abstract Syntax Tree (AST)
        tree = ast.parse(expr, mode='eval')
        # Compile the AST into a code object
        compiled = compile(tree, filename='<ast>', mode='eval')
        # Safely evaluate the expression (basic arithmetic only)
        return eval(compiled, {"__builtins__": None}, {})
    except Exception as e:
        # Handle errors in parsing or evaluation
        print(f"An error occurred: {e}")
        return None

def demonstrate_rounding(user_input):
    # Find machine epsilon for default float type (double precision)
    epsilon = find_machine_epsilon()
    
    print("Machine epsilon:", epsilon)
    
    # Evaluate the user's input
    result = safe_eval(user_input)
    if result is not None:
        # Show the result of the input evaluation
        print(f"The evaluated result is: {result}")
        # Demonstrate rounding with the result
        print(f"{result} + epsilon/2 (rounded):", result + epsilon/2)
        print(f"{result} + epsilon (rounded):", result + epsilon)
    else:
        print("The input was not a valid number or expression.")

if __name__ == "__main__":
    user_input = input("Enter a number or an equation (e.g., '0.2+0.3' or '44'): ")
    demonstrate_rounding(user_input)
