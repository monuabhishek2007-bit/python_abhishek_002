"""Unit Converter.

Supports Length, Weight, and Temperature conversions.
"""


def convert_length(value, from_unit, to_unit):
    """Convert a length from one unit to another."""
    to_meters = {
        "km": 1000,
        "m": 1,
        "cm": 0.01,
        "mm": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254
    }

    meters = value * to_meters[from_unit]
    return meters / to_meters[to_unit]


def convert_weight(value, from_unit, to_unit):
    """Convert a weight from one unit to another."""
    to_grams = {
        "kg": 1000,
        "g": 1,
        "mg": 0.001,
        "pound": 453.592,
        "ounce": 28.3495
    }

    grams = value * to_grams[from_unit]
    return grams / to_grams[to_unit]


def convert_temperature(value, from_unit, to_unit):
    """Convert a temperature from one unit to another."""
    if from_unit == to_unit:
        return value

    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:
        return None

    if to_unit == "celsius":
        return celsius

    if to_unit == "fahrenheit":
        return (celsius * 9 / 5) + 32

    if to_unit == "kelvin":
        return celsius + 273.15

    return None


def main():
    """Run the unit converter program."""
    print("===== Unit Converter =====")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")

    choice = input("Choose a category (1/2/3): ")

    if choice == "1":
        print("Available units: km, m, cm, mm, mile, yard, foot, inch")

        from_unit = input("Convert from: ").strip().lower()
        to_unit = input("Convert to: ").strip().lower()
        value = float(input("Enter value: "))

        result = convert_length(value, from_unit, to_unit)

        print(f"{value} {from_unit} = {result:.4f} {to_unit}")

    elif choice == "2":
        print("Available units: kg, g, mg, pound, ounce")

        from_unit = input("Convert from: ").strip().lower()
        to_unit = input("Convert to: ").strip().lower()
        value = float(input("Enter value: "))

        result = convert_weight(value, from_unit, to_unit)

        print(f"{value} {from_unit} = {result:.4f} {to_unit}")

    elif choice == "3":
        print("Available units: celsius, fahrenheit, kelvin")

        from_unit = input("Convert from: ").strip().lower()
        to_unit = input("Convert to: ").strip().lower()
        value = float(input("Enter value: "))

        result = convert_temperature(value, from_unit, to_unit)

        if result is not None:
            print(f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            print("Invalid temperature unit!")

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
