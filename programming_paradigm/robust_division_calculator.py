def safe_divide(numerator, denominator):
    try:
        print("DEBUG: Inside try block")
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"Result: {result}"
    except ValueError:
        return "Error: Both inputs must be numeric."
    except ZeroDivisionError:
        return "Custom ZeroDivisionError message."
