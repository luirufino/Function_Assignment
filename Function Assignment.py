import math

def circle_area(radius, pi=math.pi):
    return pi * radius ** 2
def total_due(money, rate):
    return money + (money * (rate / 100))
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)
def main():
    radii = [10, 6, 24, 2, 1]
    print("Circle Area Tests:")
    for radius in radii:
        print(f"Radius: {radius}, Area: {circle_area(radius):.2f}")
    money_values = [20, 54, 68]
    rates = [6, 4, 8]
    print("\nTotal Due Tests:")
    for money, rate in zip(money_values, rates):
        print(f"Money: {money}, Rate: {rate}%, Total Due: {total_due(money, rate):.2f}")
    fahrenheit_values = [32, 80, 73, 42]
    print("\nFahrenheit to Celsius Tests:")
    for fahrenheit in fahrenheit_values:
        print(f"Fahrenheit: {fahrenheit}, Celsius: {fahrenheit_to_celsius(fahrenheit):.5f}")

if __name__ == "__main__":
    main()
