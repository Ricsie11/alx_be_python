def safe_divide(numerator, denominator):
    try:
        print("DEBUG: Inside try block")
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"Result: {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
