# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"Result: {result}"
    except ValueError:
        return "Error: Both inputs must be numeric."
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
