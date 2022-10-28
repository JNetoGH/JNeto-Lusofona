class Calculator:

    def calculate(self, op: str, num1: float, num2: float) -> None:
        if op == "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        elif op == "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        elif op == "/":
            print(f"{num1} / {num2} = {num1 / num2}")
        elif op == "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        else:
            print("operation not recognized")

    def is_prime(self, num: int):
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} is not prime, division found with {i}")
                return
        print(f"{num} is prime")


calculator: Calculator = Calculator()
calculator.calculate("+", 5, 5)
calculator.calculate("-", 5, 8)
calculator.calculate("/", 5, 2)
calculator.calculate("*", 5, 4.5)
print()
calculator.is_prime(10)
calculator.is_prime(5)
calculator.is_prime(55)
calculator.is_prime(7)