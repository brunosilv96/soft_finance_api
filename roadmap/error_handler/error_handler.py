from ...exceptions.zero_division_exception import ZeroDivisionException

def divide(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionException()
    
    return a / b

try:
    # result = divide(10, 2)
    result = divide(10, 0)
    print(result)

except ZeroDivisionException as error:
    print("Error:", error)

finally:
    print("Divisão finalizada")