"""Calculator module that provides basic arithmetic operations with history tracking."""

from typing import List, Tuple


class Calculation:
    """Class to store a single arithmetic operation."""  # pylint: disable=too-few-public-methods

    def __init__(self, operation: str, operand1: float, operand2: float, result: float):
        """Initialize a calculation instance."""
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result


class Calculator:
    """Basic calculator class with history tracking."""

    history: List[Calculation] = []

    @staticmethod
    def add(a: float, b: float) -> float:
        """Perform addition and store the result."""
        result = a + b
        Calculator._store_calculation("add", a, b, result)
        return result

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Perform subtraction and store the result."""
        result = a - b
        Calculator._store_calculation("subtract", a, b, result)
        return result

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Perform multiplication and store the result."""
        result = a * b
        Calculator._store_calculation("multiply", a, b, result)
        return result

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Perform division and store the result. Raises an error for division by zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        Calculator._store_calculation("divide", a, b, result)
        return result

    @classmethod
    def _store_calculation(cls, operation: str, a: float, b: float, result: float) -> None:
        """Stores a calculation in history."""
        cls.history.append(Calculation(operation, a, b, result))

    @classmethod
    def get_last_calculation(cls) -> Tuple[str, float, float, float]:
        """Retrieves the last calculation from history."""
        if cls.history:
            last_calc = cls.history[-1]
            return last_calc.operation, last_calc.operand1, last_calc.operand2, last_calc.result
        return "No calculations yet", 0, 0, 0

    @classmethod
    def clear_history(cls) -> None:
        """Clears the calculation history."""
        cls.history.clear()

    @classmethod
    def print_history(cls) -> None:
        """Prints the calculation history."""
        if not cls.history:
            print("No calculations in history.")
            return
        for calc in cls.history:
            print(f"{calc.operand1} {calc.operation} {calc.operand2} = {calc.result}")


### **User Input Interface**
def main():
    """Main function for user interaction."""
    last_result = None
    while True:
        print("\nWelcome to Basic Calculator:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Check Calculation History")
        print("6. Check Last Calculation")
        print("7. Clear History")
        print("8. Use Last Result in New Calculation")
        print("9. Exit")

        choice = input("Enter choice: ").strip()

        if choice in ('1', '2', '3', '4'):
            if last_result is not None:
                use_last = input("Use last result? (y/n): ").strip().lower()
                if use_last == 'y':
                    a = last_result
                else:
                    a = float(input("Enter first number: "))
            else:
                a = float(input("Enter first number: "))

            b = float(input("Enter second number: "))

            if choice == '1':
                last_result = Calculator.add(a, b)
            elif choice == '2':
                last_result = Calculator.subtract(a, b)
            elif choice == '3':
                last_result = Calculator.multiply(a, b)
            elif choice == '4':
                try:
                    last_result = Calculator.divide(a, b)
                except ZeroDivisionError as e:
                    print(e)
                    last_result = None

            print("Result:", last_result)

        elif choice == '5':
            Calculator.print_history()
        elif choice == '6':
            print("Last Calculation:", Calculator.get_last_calculation())
        elif choice == '7':
            Calculator.clear_history()
            print("History Cleared.")
        elif choice == '8':
            if last_result is not None:
                print("Using last result in new calculation.")
            else:
                print("No previous calculation available.")
        elif choice == '9':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
