def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Is not possible divide from zero")
    
    return a / b

try:
    # result = divide(10, 2)
    result = divide(10, 0)
    print(result)

except ValueError as error:
    print("Error:", error)

finally:
    print("Divisão finalizada")